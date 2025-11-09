# placeholder: gym-style trading environment
class TradingEnv:
    def __init__(self, *args, **kwargs):
        pass

    def reset(self):
        return None

    def step(self, action):
        obs, reward, done, info = None, 0.0, True, {}
        return obs, reward, done, info
