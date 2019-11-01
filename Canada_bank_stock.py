#!/usr/bin/env python
# coding: utf-8

# # Finance Project
# 
# * TD Bank (TD)
# * BMO Bank (BMO)
# * RBC Bank (RY)
# * Bank of Nova Scotia (BNS)
# * CIBC Bank (CM)

# In[12]:


from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly
import cufflinks as cf
cf.go_offline()
get_ipython().run_line_magic('matplotlib', 'inline')




start = datetime.datetime(2011, 1, 1)
end = datetime.datetime(2016, 1, 1)




#Bank of Montreal
BMO = data.DataReader("BMO", 'yahoo', start, end)

#Bank of Nova Scotia
BNS = data.DataReader("BNS", 'yahoo', start, end)

#CIBC 
CM = data.DataReader("CM", 'yahoo', start, end)

#RBC
RY = data.DataReader("RY", 'yahoo', start, end)

#Toronto Dominion Bank
TD = data.DataReader("TD", 'yahoo', start, end)





tickers = ['BMO', 'BNS', 'CM', 'RY', 'TD'] #list of tickers




bank_stocks = pd.concat([BMO, BNS, CM, RY, TD], axis = 1, keys= tickers)
bank_stocks.columns.names = ['Bank Ticker Symbol', 'Stock Info']



bank_stocks.head()



RY[['Open','Close']].iplot(kind='spread') 




for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()




sns.heatmap(bank_stocks.xs(key='Open',axis=1,level='Stock Info').corr(),annot=True)

