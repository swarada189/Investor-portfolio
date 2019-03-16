#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime
from sys import exit
import fix_yahoo_finance as yf
yf.pdr_override() 


# In[19]:


#import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si


# In[20]:


#Initialise dates
start_date="2018-09-12"
end2 = "2018-09-13"
end_date="2019-03-15"
today=datetime.date.today()


# In[25]:


#Populate stocks dataframe using excel
stockPF = pd.read_excel('Portfolio.xlsx')
stockPF["CUR_PRICE"] = 0


# In[26]:



stockPF["CUR_PRICE"][0]= si.get_live_price('BARC.L')
stockPF["CUR_PRICE"][1]= si.get_live_price('VOD.L')
stockPF["CUR_PRICE"][2]= si.get_live_price('SSE.L')
stockPF["CUR_PRICE"][3]= si.get_live_price('MCRO.L')


# In[27]:


stockPF["FUND_VAL"] = stockPF["QTY"] * stockPF["CUR_PRICE"]
stockPF["PRO/LOSS"] = stockPF["CUR_PRICE"] - stockPF["PCH_PRICE"]
stockPF["PERC"] = stockPF["PRO/LOSS"] / stockPF["PCH_PRICE"]
stockPF


# In[28]:


#comparison of net portfolio value with index
prevPF = (stockPF["QTY"] * stockPF["PCH_PRICE"]).sum()
currPF = (stockPF["FUND_VAL"]).sum()
delPF = (currPF - prevPF)/prevPF


# In[34]:


prevID = pdr.get_data_yahoo('^FTSE',start=start_date,end=start_date)
prevID = float(prevID["Close"])
  


# In[35]:


currID = pdr.get_data_yahoo('^FTSE',start="2019-03-16",end="2019-03-17")
currID = float(currID["Close"])
delID = (currID - prevID)/prevID
if delID < 0:
    neg = 1
else:
    neg=0


# In[36]:


stockPF["CONTRI"] = (stockPF["PRO/LOSS"]*stockPF["QTY"])/prevPF
stockPF


# In[42]:


import json
data =  {'acc_value':float(currPF),'buying_power':190000,'cash':210000,'annual_ret':0.49,
         'ftse':currID,
         'del_index':delID,
         'del_pf':delPF,
         'ID_updown':neg}
data['stocks'] = []
for i in range(0,4):
    data['stocks'].append({'company':stockPF['COMP'][i],
                           'symbol':stockPF['SYM'][i],
                           'pprice':float(stockPF['PCH_PRICE'][i]),
                           'qty':float(stockPF['QTY'][i]),
                          'cprice':float(stockPF['CUR_PRICE'][i]),
                            'fund':float(stockPF['FUND_VAL'][i]),
                          'pro-loss':float(stockPF['PRO/LOSS'][i]),
                          'perc':float(stockPF['PERC'][i]),
                          'contri':float(stockPF['CONTRI'][i])})
with open('findata.json','w') as outfile:
    json.dump(data,outfile)






