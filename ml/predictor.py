TICKERS = {
    "SPY": "high",
    "QQQ": "high",
    "GLD": "medium",
    "VNQ": "medium",
    "BND": "low",
    "TIP": "low",
}


def recommend_portfolio(risk_level: str, horizon_years: int) -> dict:
    # build a risk threshold for relative scaling
    risk_threshold = 0

    if risk_level == "high":
        risk_threshold += 3
    elif risk_level == "medium":
        risk_threshold += 2
    elif risk_level == "low":
        risk_threshold += 1
    
    risk_threshold *= horizon_years

    # get our risk bucket, which defines our portfolios risk tolerance
    risk_bucket = get_risk_bucket(risk_threshold)

    # delegate portfolio based on risk
    # risk threshold 1 - 10
    if risk_bucket == "conservative":
        pass
    # 11 - 20
    elif risk_bucket == "balanced":
        pass
    # 21 - 30
    elif risk_bucket == "growth":
        pass
    # 30+
    else:
        pass

def get_risk_bucket(threshold: int) -> str:
    # risk bucket function for cleaner, more modular code
    if threshold <= 10:
        return "conservative"
    elif threshold <= 20:
        return "balanced"
    elif threshold <= 30:
        return "growth"
    else:
        return "aggressive"