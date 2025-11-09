# placeholder: time-varying weights for rewards
class RewardScheduler:
    def __init__(self, total_steps=100000, mode="fixed"):
        self.T, self.mode = max(1, total_steps), mode

    def _alpha(self, t):
        x = min(max(t/self.T, 0.0), 1.0)
        if self.mode == "linear":
            return x
        if self.mode == "cosine":
            import math
            return 0.5 - 0.5*math.cos(math.pi*x)
        return 0.0

    def weights_at(self, t, base):
        a = self._alpha(t)
        return {
            "w_pnl":   base["w_pnl"],
            "w_cost":  base["w_cost"],
            "w_dd":    base["w_dd"] + a,
            "w_sharpe":base["w_sharpe"] + a,
        }

