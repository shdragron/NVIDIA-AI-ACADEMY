# 1_3_frozen_lake.py
import gym


def gym_basic():
    env = gym.make('FrozenLake-v1', render_mode='human')

    print(env.action_space)
    print(env.observation_space)

    print(env.action_space.n)
    print(env.observation_space.n)

    env.reset()
    env.render()

    result = env.step(1) # action
    env.render()

    print(result)
    # state reward done terminated info
    # (1, 0.0, False, False, {'prob': 0.3333333333333333})


def frozen_lake_basic():
    env = gym.make('FrozenLake-v1', render_mode='human', is_slippery=False)

    env.reset()
    env.render()

    # 퀴즈
    # step 함수를 사용해서 캐릭터를 목적지까지 이동시켜주세요
    LEFT, DOWN, RIGHT, UP = 0, 1, 2, 3

    for action in [RIGHT, RIGHT, DOWN, DOWN, DOWN, RIGHT]:
        result = env.step(action)
        env.render()

        print(result)


# gym_basic()
frozen_lake_basic()
