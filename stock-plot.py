from yahoofinancials import YahooFinancials
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

SP500 = '^GSPC'
ref = YahooFinancials('^GSPC')

symbol = "NEE"
stock = YahooFinancials(symbol)
#print(data)
data = stock.get_historical_price_data("2018-01-01","2019-02-15","weekly")
ref_data = ref.get_historical_price_data("2018-01-01","2019-02-15","weekly")
plt.figure(figsize=(16,8),dpi=200)
ax = plt.subplot(111)
close = np.array([x["close"] for x in data[symbol]["prices"]])
ax.plot([x["date"] for x in data[symbol]["prices"]],
        close/close[0]*100, label=symbol)
close = np.array([x["close"] for x in ref_data[SP500]["prices"]])
ax.plot([x["date"] for x in ref_data[SP500]["prices"]],
        close/close[0]*100, label="SP500")
plt.savefig("test.png")


#ticker = 'AAPL'
#yahoo_financials = YahooFinancials(ticker)
#
#balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
#print(balance_sheet_data_qt)
