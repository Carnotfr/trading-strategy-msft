#!/usr/bin/env python
# coding: utf-8

# # A buy/sell signal for Microsoft stock

# This code downloads historical stock data for Microsoft from Yahoo Finance using the yfinance library. It then calculates the daily percentage change in the adjusted close price, and based on that, creates a buy/sell signal for the stock.
# 
# The buy/sell signal is created by setting a "signal" to 1 if the price increase is positive and 0 if it's negative. The signal is then differenced to get the position changes.
# 
# Using the buy/sell signals, the code creates a portfolio that invests in the Microsoft stock. The portfolio's initial capital is set to $253.17. It calculates the portfolio's value and plots it in a graph.
# 
# Finally, the code plots the portfolio's total value, highlighting the buy/sell signals with upward (^) and downward (v) arrows.

# In[58]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[59]:


import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[60]:


# Download Microsoft stock price data from Yahoo Finance
msft = yf.download("MSFT", start="2022-01-01", end="2023-04-12")
print(msft)


# In[61]:


# Create a DataFrame to store the trading signals
msft_signal = pd.DataFrame(index = msft.index)
msft_signal['Price'] = msft['Adj Close']
msft_signal['Daily_Difference'] = msft_signal['Price'].diff()
msft_signal['Signal'] = np.where(msft_signal['Daily_Difference'][:] > 0, 1.0, 0.0)
msft_signal['Positions'] = msft_signal['Signal'].diff()


# In[62]:


print(msft_signal)


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Create a figure object and add a subplot
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Microsoft price in $')


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Plot the stock price data with buy/sell signals
msft_signal['Price'].plot(ax=ax1, color='m', lw=3.)
ax1.plot(msft_signal.loc[msft_signal.Positions == 1.0].index,
         msft_signal.Price[msft_signal.Positions == 1.0],
         '^', markersize=5, color='r')
ax1.plot(msft_signal.loc[msft_signal.Positions == -1.0].index,
         msft_signal.Price[msft_signal.Positions == -1.0],
         'v', markersize=5, color='k')

# Set the plot title and display the plot
plt.title('Trading Strategy for Microsoft Stock')
#plt.show()


# In[46]:


#Since I am unable to display the plot without splitting the cells, I am going to write the whole code above in one cell
get_ipython().run_line_magic('matplotlib', 'inline')

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Download Microsoft stock price data from Yahoo Finance
msft = yf.download("MSFT", start="2022-01-01", end="2023-04-12")

# Create a DataFrame to store the trading signals
msft_signal = pd.DataFrame(index = msft.index)
msft_signal['Price'] = msft['Adj Close']
msft_signal['Daily_Difference'] = msft_signal['Price'].diff()
msft_signal['Signal'] = np.where(msft_signal['Daily_Difference'][:] > 0, 1.0, 0.0)
msft_signal['Positions'] = msft_signal['Signal'].diff()

# Create a figure object and add a subplot
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Microsoft price in $')

# Plot the stock price data with buy/sell signals
msft_signal['Price'].plot(ax=ax1, color='m', lw=3.)
ax1.plot(msft_signal.loc[msft_signal.Positions == 1.0].index,
         msft_signal.Price[msft_signal.Positions == 1.0],
         '^', markersize=5, color='r')
ax1.plot(msft_signal.loc[msft_signal.Positions == -1.0].index,
         msft_signal.Price[msft_signal.Positions == -1.0],
         'v', markersize=5, color='k')

# Set the plot title and display the plot
plt.title('Trading Strategy for Microsoft Stock')
plt.show()


# In[49]:


#Let's set an initial capital
Capital = float(253.17)
Positions = pd.DataFrame(index=msft_signal.index).fillna(0.0)
Portfolio = pd.DataFrame(index=msft_signal.index).fillna(0.0)
print(Positions)


# In[50]:


print(Portfolio)


# In[51]:


Positions['MSFT'] = msft_signal['Signal']
Portfolio['Positions'] = (Positions.multiply(msft_signal['Price'], axis=0))
Portfolio['Cash'] = Capital - (Positions.diff().multiply(msft_signal['Price'], axis=0)).cumsum()
Portfolio['Total'] = Portfolio['Positions'] + Portfolio['Cash']
Portfolio.plot()
plt.show()


# In[57]:


fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')
Portfolio['Total'].plot(ax=ax1, lw=3.)
ax1.plot(Portfolio.loc[msft_signal.Positions == 1.0].index,Portfolio.Total[msft_signal.Positions == 1.0],'^', markersize=10, color='m')
ax1.plot(Portfolio.loc[msft_signal.Positions == -1.0].index,Portfolio.Total[msft_signal.Positions == -1.0],'v', markersize=10, color='k')

plt.show()


# In[ ]:




