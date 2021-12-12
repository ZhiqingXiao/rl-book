# ==== imports ====

import time
import datetime as dt
import math
import itertools

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.initializers import RandomNormal
import msgpackrpc
import airsim


# ==== Environment ====

class AirSimCarEnv:
    def __init__(self):
        self.connect()


    def connect(self):
        # 连接正在运行的 AirSim
        self.car_client = airsim.CarClient()
        self.car_client.confirmConnection()
        self.car_client.enableApiControl(True)


    def get_image(self):
        # 获得图像信息
        # while True: # 有的时候会失败，这时候重试就好
        #     try:
        image_request = airsim.ImageRequest(0,
                airsim.ImageType.Scene, False, False)
        image_response = self.car_client.simGetImages(
                [image_request,])[0]
        image1d = np.frombuffer(image_response.image_data_uint8,
                dtype=np.uint8)
        image_rgba = image1d.reshape(image_response.height,
                image_response.width, -1)
        #         break
        #     except:
        #         print('获取图像失败，重试')
        return image_rgba[76:135,0:255,0:3].astype(float)


    def control(self, throttle=0, steering=0, brake=0, handbrake=False):
        # 设置油门、方向和刹车
        car_controls = airsim.CarControls(throttle=throttle,
                steering=steering, brake=brake, handbrake=handbrake)
        self.car_client.setCarControls(car_controls)


    def get_car_state(self):
        # 获取车辆状态（速度等）
        return self.car_client.getCarState()


    def get_roads(self, include_corners=True):
        # 获得地图上的路的信息
        lines = [
                [[-128, -121], [-128, 119]],
                [[-120, -129], [120, -129]],
                [[-120, 127], [120, 127]],
                [[128, -121], [128, 119]],
                [[0, -121], [0, 119]],
                [[-120, 0], [120, 0]],
                [[80, -124], [80, -5]],
                ]
        if include_corners: # 路的拐弯
            for x0, x1 in [[-128, -120], [0, -8], [0, 8], [120, 128]]:
                corners = [
                        [[x0, -121], [x1, -129]],
                        [[x0, -8], [x1, 0]],
                        [[x0, 8], [x1, 0]],
                        [[x0, 119], [x1, 127]],
                        ]
                lines += corners
            for x0, x1 in [[80, 75], [80, 85]]:
                corners = [
                        [[x0, -124], [x1, -129]],
                        [[x0, -5], [x1, 0]],
                        ]
                lines += corners
        roads = [(np.array(p), np.array(q)) for p, q in lines]
        return roads


    def get_start_pose(self, random=True, verbose=True):
        # 在路上选择一个起始位置和方向
        if not random: # 固定选择默认的起始位置
            position = np.array([0., 0.])
            yaw = 0.
        else: # 随机选择一个位置
            if not hasattr(self, 'roads_without_corners'):
                self.roads_without_corners = self.get_roads(
                        include_corners=False)

            # 计算位置
            road_index = np.random.choice(len(self.roads_without_corners))
            p, q = self.roads_without_corners[road_index]
            t = np.random.uniform(0.3, 0.7)
            position = t * p + (1. - t) * q

            # 计算朝向
            if np.isclose(p[0], q[0]): # 与 Y 轴平行
                yaws = [0.5 * math.pi, -0.5 * math.pi]
            elif np.isclose(p[1], q[1]): # 与 X 轴平行
                yaws = [0., math.pi]
            yaw = np.random.choice(yaws)

        if verbose:
            print('起始位置 = {}, 方向 = {}'.format(position, yaw))

        position = airsim.Vector3r(position[0], position[1], -0.6)
        orientation = airsim.to_quaternion(pitch=0., roll=0., yaw=yaw)
        pose = airsim.Pose(position, orientation)
        return pose


    def reset(self, explore_start=False, brake_confirm=True,
            start_accelerate=True, max_epoch_time=None, verbose=True):
        if verbose:
            print('开始新回合')

        # 起始探索
        start_pose = self.get_start_pose(random=explore_start)

        if brake_confirm:
            # 预设值起始位置, 刹车，并等待车变的稳定
            # 因为 simSetVehiclePose() 不能设置速度，只能选择刹车再等待
            self.car_client.simSetVehiclePose(start_pose, True)
            env.control(brake=1, handbrake=True)
            time.sleep(4)

        # 再次设置初始位置
        if verbose:
            print('设置初始位置')
        self.car_client.simSetVehiclePose(start_pose, True)

        if start_accelerate:
            # 让车加速一段时间，否则如果车的速度太小，后面会认为回合结束
            if verbose:
                print('直行一段时间')
            env.control(throttle=1)
            time.sleep(10)

        # 回合开始时间和预期结束时间
        self.start_time = dt.datetime.now()
        self.end_time = None
        if max_epoch_time:
            self.expected_end_time = self.start_time + \
                    dt.timedelta(seconds=max_epoch_time)
        else:
            self.expected_end_time = None


    def get_reward(self):
        # 计算奖励，并评估回合是否结束

        collision_info = self.car_client.simGetCollisionInfo() # 碰撞信息
        if collision_info.has_collided: # 如果撞车了，没有奖励，回合结束
            self.end_time = dt.datetime.now()
            return 0.0, True, {'message' : 'collided'}

        car_state = self.car_client.getCarState() # 获取车辆速度信息
        if car_state.speed < 2: # 如果停车了，没有奖励，回合结束
            self.end_time = dt.datetime.now()
            return 0.0, True, {'speed' : car_state.speed}

        car_point = car_state.kinematics_estimated.position. \
                to_numpy_array() # 获取车辆位置信息

        if not hasattr(self, 'roads'):
            self.roads = self.get_roads()

        # 计算位置到各条路的最小距离
        distance = float('+inf')
        for p, q in self.roads:
            # 点到线段的最小距离
            frac = np.dot(car_point[:2] - p, q - p) / np.dot(q - p, q - p)
            clipped_frac = np.clip(frac, 0., 1.)
            closest = p + clipped_frac * (q - p)
            dist = np.linalg.norm(car_point[:2] - closest)
            distance = min(dist, distance) # 更新最小距离

        reward = math.exp(-1.2 * distance) # 基于距离的奖励函数

        if distance > 3.5: # 偏离路面太远，回合结束
            self.end_time = dt.datetime.now()
            return reward, True, {'distance' : distance}

        # 判断是否超时
        now = dt.datetime.now()
        if self.expected_end_time is not None and now > \
                self.expected_end_time:
            self.end_time = now
            info = {'start_time' : self.start_time,
                    'end_time' : self.end_time}
            return reward, True, info # 回合超时结束

        return reward, False, {}



# ==== Agent ====

class DQNReplayer:
    def __init__(self, capacity):
        self.memory = pd.DataFrame(index=range(capacity),
                columns=['observation', 'action', 'reward',
                'next_observation', 'done'])
        self.i = 0
        self.count = 0
        self.capacity = capacity

    def store(self, *args):
        self.memory.loc[self.i] = args
        self.i = (self.i + 1) % self.capacity
        self.count = min(self.count + 1, self.capacity)

    def sample(self, size):
        indices = np.random.choice(self.count, size=size)
        return (np.stack(self.memory.loc[indices, field]) for field in \
                self.memory.columns)

class DQNAgent():
    def __init__(self, gamma=0.99, batch_size=32,
            replayer_capacity=2000, random_initial_steps=50,
            weight_path=None, train_conv=True,
            epsilon=1., min_epsilon=0.1, epsilon_decrease_rate=0.003):
        self.action_n = 5
        self.gamma = gamma

        # 经验回放
        self.replayer = DQNReplayer(capacity=replayer_capacity)
        self.batch_size = batch_size
        self.random_initial_steps = random_initial_steps

        # 探索参数
        self.epsilon = epsilon
        self.min_epsilon = min_epsilon
        self.epsilon_decrease_rate = epsilon_decrease_rate

        # 搭建网络
        self.evaluate_net = self.build_network(weight_path=weight_path,
                train_conv=train_conv)
        self.target_net = self.build_network()
        self.target_net.set_weights(self.evaluate_net.get_weights())

    def build_network(self, activation='relu', weight_path=None,
                train_conv=True, verbose=True):
        inputs = keras.Input(shape=(59, 255, 3))
        x = inputs

        # 卷积层
        for filte in [16, 32, 32]:
            z = keras.layers.Conv2D(filte, 3, padding='same',
                    activation=activation,
                    trainable=train_conv)(x)
            x = keras.layers.MaxPooling2D(pool_size=2)(z)

        y = keras.layers.Flatten()(x)

        # 全连接层
        x = keras.layers.Dropout(0.2)(y)
        z = keras.layers.Dense(128, activation=tf.nn.relu,
                kernel_initializer=RandomNormal(stddev=0.01))(x)
        y = keras.layers.Dropout(0.2)(z)
        outputs = keras.layers.Dense(self.action_n,
                kernel_initializer=RandomNormal(stddev=0.01))(y)

        net = keras.Model(inputs=inputs, outputs=outputs)
        net.compile(optimizer='adam', loss='mse')

        if verbose:
            net.summary()

        if weight_path:
            net.load_weights(weight_path)
            if verbose:
                print('载入网络权重 {}'.format(weight_path))

        return net


    def decide(self, observation, random=False):
        if random or np.random.rand() < self.epsilon:
            return np.random.randint(self.action_n)
        observations = observation[np.newaxis]
        qs = self.evaluate_net.predict(observations)
        return np.argmax(qs)


    def action2control(self, action, car_state):
        # 将动作转换为控制信号
        steering = 0.5 * action - 1. # 方向，可取 -1, -0.5, 0, 0.5, 1
        if car_state.speed > 9:
            return 0, steering, 1
        else:
            return 1, steering, 0


    def learn(self, observation, action, reward, next_observation, done):
        agent.replayer.store(observation, action, reward, next_observation,
                done) # 存储经验

        if self.replayer.count < self.random_initial_steps:
            return # 还没到存足够多的经验，先不训练神经网络

        observations, actions, rewards, next_observations, dones = \
                self.replayer.sample(self.batch_size) # 经验回放

        next_qs = self.target_net.predict(next_observations)
        next_max_qs = next_qs.max(axis=-1)
        us = rewards + self.gamma * next_max_qs * (1. - dones)
        targets = self.evaluate_net.predict(observations)
        targets[np.arange(us.shape[0]), actions] = us
        self.evaluate_net.fit(observations, targets, verbose=0)

        if done:
            self.target_net.set_weights(self.evaluate_net.get_weights())

        # 减小 epsilon 的值
        self.epsilon -= self.epsilon_decrease_rate
        self.epsilon = max(self.epsilon, self.min_epsilon)


# ==== Interact ====

def play_once(env, agent, explore_start=False, random=False, train=False,
    max_epoch_time=None, wait_delta_sec=0.01, verbose=True):

    # 启动新回合，在地图上选择一个地方，并让汽车前进一段
    env.reset(explore_start=explore_start, max_epoch_time=max_epoch_time)

    # 正式开始学习
    for step in itertools.count():

        image = env.get_image()
        car_state = env.get_car_state()
        action = agent.decide(image, random=random)

        # 根据动作影响环境
        throttle, steering, brake = agent.action2control(action, car_state)
        if verbose:
            print('动作 = {}, 速度 = {}, 油门 = {}, 方向 = {}, 刹车 = {}' \
                    .format(action, car_state.speed, throttle, steering,
                    brake))
        env.control(throttle, steering, brake)

        # 等待一段时间
        time.sleep(wait_delta_sec)

        # 获得更新后的观测、奖励和回合结束指示
        next_image = env.get_image()
        reward, done, info = env.get_reward()

        # 如果回合刚开始就结束了，就不是靠谱的回合
        if step == 0 and done:
            if verbose:
                print('不成功的回合，放弃保存')
            break

        if train: # 根据经验学习
            agent.learn(image, action, reward, next_image, done)

        # 回合结束
        if done:
            if verbose:
                print('回合 从 {} 到 {} 结束. {}'.format(
                        env.start_time, env.end_time, info))
            break



# ==== Train & Test ====

"""
从头开始训练，需要训练几周
"""
weight_path = None # 载入权重数据的位置
train_conv = True # 是否训练卷积层
max_epoch_time = 30. # 最长回合时间
random_initial_steps = 1000 # 随机运行的初始步数
train = True # 是否训练

"""
预训练的结果，只需要再训练全连接层，再训练数小时即可
"""
weight_path = 'pretrain_weights.h5'
train_conv = False
max_epoch_time = 30.
random_initial_steps = 50
train = True

"""
训练好的结果，直接能用
"""
weight_path = 'weights.h5'
train_conv = False
max_epoch_time = None
random_initial_steps = 0
train = False




env = AirSimCarEnv()
agent = DQNAgent(weight_path=weight_path, train_conv=train_conv,
        random_initial_steps=random_initial_steps)

if train:
    print('开始训练')
    while True: # 无限循环，永不停止。需要手动中断
        try:
            # 判断是否用随机动作填充经验库
            random = agent.replayer.count < random_initial_steps

            play_once(env, agent, explore_start=True, random=random,
                    train=True, max_epoch_time=max_epoch_time)

        # 极少数情况下 AirSim 会停止工作，需要重新启动并连接
        except msgpackrpc.error.TimeoutError:
            print('与 AirSim 连接中断。开始重新链接')
            env.connect()
else:
    print('开始测试')
    agent.epsilon = 0. # 取消探索
    play_once(env, agent, max_epoch_time=max_epoch_time)


