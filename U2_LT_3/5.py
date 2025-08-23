# 5. Stock Price Simulation (Reshaping + Aggregation + Boolean indexing)
# A financial analyst wants to study stock price changes of 4 companies over 10 days.
# • Generate a 4x10 NumPy array with random floats between 100 and 500 (stock prices).
# • Calculate the daily average stock price across all companies.
# • Find the company with the highest average stock price over the 10 days.
# • Use Boolean indexing to filter out all prices above 450.

import numpy as np

stock_prices = np.random.uniform(100, 500, size=(4, 10)).round(2)
daily_avg = stock_prices.mean(axis=0)
company_avg = stock_prices.mean(axis=1)
highest_avg = np.argmax(company_avg)
above_450 = stock_prices[stock_prices > 450]

print("=====================================================")
print("5. Stock Price Simulation:")
print("=====================================================")
print("Stock prices:\n", stock_prices)
print("=====================================================")
print("Daily average prices:", daily_avg)
print("=====================================================")
print("Company with highest average stock price:", highest_avg)
print("=====================================================")
print("Prices above 450:", above_450)
print("=====================================================")