import matplotlib.pyplot as plt
import seaborn as sns

# Plot the closing price over time
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Close Price')
plt.title(f'{symbol} Stock Price')
plt.xlabel('Date')
plt.ylabel('Close Price USD')
plt.legend()
plt.show()

# Calculate and plot moving averages
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()

plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['MA50'], label='50-Day Moving Average')
plt.plot(stock_data['MA200'], label='200-Day Moving Average')
plt.title(f'{symbol} Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Close Price USD')
plt.legend()
plt.show()
