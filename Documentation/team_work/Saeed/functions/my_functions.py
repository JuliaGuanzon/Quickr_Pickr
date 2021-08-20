#!/usr/bin/env python
# coding: utf-8

# In[1]:


# http://theautomatic.net/yahoo_fin-documentation/
# pip install yahoo-fin
import yahoo_fin.stock_info as si
import yfinance as yf

# other libraries
import pandas as pd


# In[2]:


def get_tickers(index):
    if index == "dow":
        return si.tickers_dow()
    elif index == "sp500":
        return si.tickers_sp500()
    else:
        return si.tickers_nasdaq()


# In[3]:


def create_dataframe(old_df, new_df):
    for key in old_df:
        new_df = pd.concat([new_df, old_df[key]])
    return new_df


# In[4]:


def get_yf_data(alltickers, period_param, gp_param):
    result = yf.download((alltickers), period=period_param, group_by= gp_param)
    return result

