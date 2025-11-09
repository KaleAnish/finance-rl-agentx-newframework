# placeholder: metrics (Sharpe, drawdown)
def sharpe(returns, periods_per_year=252):
    if not returns: return 0.0
    import math
    mu = sum(returns)/len(returns)
    sigma = (sum((r-mu)**2 for r in returns)/max(1,len(returns)-1))**0.5
    return float((mu/(sigma+1e-12))*math.sqrt(periods_per_year))

def max_drawdown(equity):
    if not equity: return 0.0
    peak, mdd = equity[0], 0.0
    for x in equity:
        peak = max(peak, x)
        mdd = min(mdd, (x-peak)/(peak+1e-12))
    return float(mdd)
