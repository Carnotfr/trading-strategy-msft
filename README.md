# trading-strategy-msft
A buy/sell signal for Microsoft stock
This code downloads historical stock data for Microsoft from Yahoo Finance using the yfinance library. It then calculates the daily percentage change in the adjusted close price, and based on that, creates a buy/sell signal for the stock.

The buy/sell signal is created by setting a "signal" to 1 if the price increase is positive and 0 if it's negative. The signal is then differenced to get the position changes.

Using the buy/sell signals, the code creates a portfolio that invests in the Microsoft stock. The portfolio's initial capital is set to $253.17. It calculates the portfolio's value and plots it in a graph.

Finally, the code plots the portfolio's total value, highlighting the buy/sell signals with upward (^) and downward (v) arrows.
