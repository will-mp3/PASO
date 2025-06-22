TICKERS = {
    "SPY": {"risk": "high", "type": "equity"},
    "BND": {"risk": "low", "type": "bond"},
    "GLD": {"risk": "medium", "type": "commodity"},
    "QQQ": {"risk": "high", "type": "tech"},
    "VNQ": {"risk": "medium", "type": "real_estate"},
}

def recommend_portfolio(risk_level: str, horizon_years: int) -> dict:
    pass