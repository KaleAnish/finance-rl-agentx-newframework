# placeholder: composite reward terms
class CompositeReward:
    def __init__(self, w_pnl=1.0, w_cost=1.0, w_dd=0.0, w_sharpe=0.0):
        self.w_pnl, self.w_cost, self.w_dd, self.w_sharpe = w_pnl, w_cost, w_dd, w_sharpe

    def __call__(self, pnl=0.0, cost=0.0, dd_pen=0.0, sharpe_proxy=0.0):
        return float(self.w_pnl*pnl - self.w_cost*cost - self.w_dd*dd_pen + self.w_sharpe*sharpe_proxy)
