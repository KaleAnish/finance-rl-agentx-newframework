# placeholder: SAC agent interface
class SACAgent:
    def act(self, obs): return 0.0
    def update(self, data): return {"loss_q": 0.0, "loss_pi": 0.0}
