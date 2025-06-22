from predictor import recommend_portfolio

risk = input("Enter risk level (low, medium, high): ")
horizon = int(input("Enter investment horizon (in years): "))

portfolio = recommend_portfolio(risk, horizon)
print(portfolio)