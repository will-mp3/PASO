import random

TICKERS = {
    "high": ["SPY", "QQQ", "ARKK"],
    "medium": ["GLD", "VNQ", "IWM"],
    "low": ["BND", "TIP", "SHY"]
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

    return build_portfolio(risk_bucket)


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
    
    
def build_portfolio(risk_bucket) -> dict:
    # risk threshold 1 - 10 : .1 high, .3 med, .6 low
    if risk_bucket == "conservative":
        selectedLow = random.sample(TICKERS["low"], k=1)
        selectedMed = random.sample(TICKERS["medium"], k=1)
        selectedHigh = random.sample(TICKERS["high"], k=1)

        allocation = {
            selectedLow : .6,
            selectedMed : .3,
            selectedHigh : .1,
        }

    # 11 - 20 : .3 high, .5 med, .2 low
    elif risk_bucket == "balanced":
        selectedLow = random.sample(TICKERS["low"], k=1)
        selectedMed = random.sample(TICKERS["medium"], k=1)
        selectedHigh = random.sample(TICKERS["high"], k=1)

        allocation = {
            selectedLow : .2,
            selectedMed : .5,
            selectedHigh : .3,
        }

    # 21 - 30 : .5 high, .3 med, .2 low
    elif risk_bucket == "growth":
        selectedLow = random.sample(TICKERS["low"], k=1)
        selectedMed = random.sample(TICKERS["medium"], k=1)
        selectedHigh = random.sample(TICKERS["high"], k=1)

        allocation = {
            selectedLow : .2,
            selectedMed : .3,
            selectedHigh : .5,
        }

    # 30+ : .7 high, .2 med, .1 low
    else:
        selectedLow = random.sample(TICKERS["low"], k=1)
        selectedMed = random.sample(TICKERS["medium"], k=1)
        selectedHigh = random.sample(TICKERS["high"], k=1)

        allocation = {
            selectedLow : .1,
            selectedMed : .2,
            selectedHigh : .7,
        }

    return allocation