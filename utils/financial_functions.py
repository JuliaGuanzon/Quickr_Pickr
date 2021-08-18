# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Import necessary libraries
import pandas as pd
import yfinance as yf
import datetime as dt
import numpy as np
from pathlib import Path
from termcolor import colored as cl
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20, 10)
plt.style.use('fivethirtyeight')


# %%
# Get advanced info for a particular stock
def get_info(ticker):
    info = yf.Ticker(ticker).info
    
    return info


# %%
# All Short-Term indicators calculated in one function
def calc_indicators (ticker):
# Downloads the data for each stock
    data = yf.download(ticker, start=start_date,end=end_date)
    data["Ticker"] = ticker
# Gets the moving average over the last 12 and 26 days
    data["MA12"] = data.Close.ewm(span=12).mean()
    data["MA26"] = data.Close.ewm(span=26).mean()
# Calculates MACD, Signal, and HIST Values
    data["MACD"] = data.MA12 - data.MA26
    data["Signal"] = data.loc[:,"MACD"].ewm(span=9).mean()
    data["HIST"] = data.loc[:,"MACD"] - data.loc[:, "Signal"]
# 50 day Simple Moving Average
    data["SMA50"] = data.loc[:,"Close"].rolling(window=50).mean()
    data["SMA50%"] = ((data.loc[:,"Close"] - data.loc[:, "SMA50"])/data.loc[:, "SMA50"])*100
# RSI Calculations
    data["Price_Change"] = data["Adj Close"].pct_change()
    data['Gains'] = data.loc[:,"Price_Change"].apply(lambda x: x if x > 0 else 0)
    data["Losses"] = data.loc[:,"Price_Change"].apply(lambda x: abs(x) if x < 0 else 0)
    data["Avg_Up"] = data.loc[:,"Gains"].ewm(com=13,adjust=False, min_periods=14).mean()
    data["Avg_Down"] = data.loc[:, "Losses"].ewm(com=13,adjust=False, min_periods=14).mean()
    data["RS"] = data.loc[:, "Avg_Up"]/data.loc[:,"Avg_Down"]
    data["RSI"] = data.loc[:,"RS"].apply(lambda x: 100 - (100/(x+1)))
    data = data.dropna()
    
    return data


# %%
# Creates a chart of prices, MACD, Signal line, and bar graph of the hist
def get_chart(ticker):
# Makes an api call via calc_indicators for the historical and indicator data
    df = calc_indicators(ticker)
# Makes 2 plots, the price on top and the MACD, Signal line, and hist on bottom
    ax1 = plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan = 1)
    ax2 = plt.subplot2grid((7,1), (5,0), rowspan = 3, colspan = 1)

    ax1.plot(df.Close)
    ax2.plot(df.MACD, color = 'black', linewidth = 1.5, label = 'MACD')
    ax2.plot(df.Signal, color = 'violet', linewidth = 1.5, label = 'SIGNAL')
# Plots the bar graph on within the second plot, showing different colors for positive and negative values
    for i in range(len(df.Close)):
        if str(df.HIST[i])[0] == '-':
            ax2.bar(df.Close.index[i], df.HIST[i], color = 'red')
        else:
            ax2.bar(df.Close.index[i], df.HIST[i], color = 'green')

    plt.legend(loc = 'lower right')


# %%
# Uses calc_indicators to get Today's Values for S&P 500
def todays_indicators():
# Create Empty lists our desired values will end up in
    stock_tick_list = []
    stock_rsi_list = []
    macd_list = []
    sig_list = []
    hist_list = []
    sma_pct = []
# Add a count so the user can know how far along they are   
    count = 0
# Iterate through the S&P 500, appending each list with the appropriate value for the most recent close
    for stock in sp500_tickers:
        stock_indicators = calc_indicators(stock)
        today = stock_indicators.iloc[-1]
        stock_tick_list.append(today["Ticker"])
        stock_rsi_list.append(today["RSI"])
        macd_list.append(today["MACD"])
        sig_list.append(today["Signal"])
        hist_list.append(today["HIST"])
        sma_pct.append(today["SMA50%"])
        count+=1
        print(count)
    frames = {"RSI" : stock_rsi_list,
             "MACD": macd_list,
             "Signal": sig_list,
             "HIST" : hist_list,
             "SMA50%": sma_pct}
    today_df = pd.DataFrame(data=frames, index=stock_tick_list)
    
    return today_df


# %%
# Sorts today_df by the indicator chosen by questionary. todays_calculations must be saved into today_df!
def sort_indicators(today_df, indicator):
    if indicator == "High RSI":
        today_df.sort_values(by=["RSI"], ascending=False,inplace=True)
    elif indicator == "Low RSI":
        today_df.sort_values(by=["RSI"], ascending=True,inplace=True)
    elif indicator == "High MACD":
        today_df.sort_values(by=["HIST"], ascending=False, inplace=True)
    elif indicator == "Low MACD":
        today_df.sort_values(by=["HIST"], ascending=True, inplace=True)
    elif indicator == "High SMA50%":
        today_df.sort_values(by=["SMA50%"], ascending=False, inplace=True)
    elif indicator == "Low SMA50%":
        today_df.sort_values(by=["SMA50%"], ascending=True, inplace=True)
    elif indicator == "Low MACD Divergence":
        divergence = [abs(i) for (i) in hist_list]
        today_df["Divergence"] = divergence
        today_df.sort_values(by=["Divergence"], ascending=True, inplace=True)
        
    return today_df


# %%
# Get S&P 500 tickers
def get_ticks():
    sp500_tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
    sp500_tickers = sp500_tickers.Symbol.to_list()
    sp500_tickers = [x.replace(".", "-") for x in sp500_tickers]
    
    return sp500_tickers


# %%
# Start and End Dates (6 months)
def get_dates():
    end_date = dt.datetime.now().date().isoformat()
    start_date = dt.datetime.now() - dt.timedelta(weeks=26)
    start_date = start_date.date().isoformat()
    
    return start_date, end_date


# %%
# Getting the Forward P/E 
def ForwardPE():
    tick_list = []
    forwardPE = []
    count = 0
    for ticker in sp500_tickers:
        info = yf.Ticker(ticker).info
        info["Ticker"] = ticker
        forwardPE.append(info["forwardPE"])
        tick_list.append(info["Ticker"])
        count+=1
        print(count)
    pe_df = pd.DataFrame(data=forwardPE, index=tick_list, columns=["Forward P/E"])
    pe_df.sort_values(by="Forward P/E", ascending=False, inplace=True)
    
    return pe_df


# %%
# # Calculating today's RSI
# def calcRSI (ticker):
#     data = yf.download(ticker, start=start_date,end=end_date, group_by="Ticker")
#     data["Ticker"] = ticker
#     data["Price_Change"] = data["Adj Close"].pct_change()
#     data['Gains'] = data.loc[:,"Price_Change"].apply(lambda x: x if x > 0 else 0)
#     data["Losses"] = data.loc[:,"Price_Change"].apply(lambda x: abs(x) if x < 0 else 0)
#     data["Avg_Up"] = data.loc[:,"Gains"].ewm(com=13,adjust=False, min_periods=14).mean()
#     data["Avg_Down"] = data.loc[:, "Losses"].ewm(com=13,adjust=False, min_periods=14).mean()
#     data["RS"] = data.loc[:, "Avg_Up"]/data.loc[:,"Avg_Down"]
#     data["RSI"] = data.loc[:,"RS"].apply(lambda x: 100 - (100/(x+1)))
#     data = data.dropna()

#     today = data.iloc[-1]

#     return today


# %%
# # Getting today's RSI for S&P 500
# def Todays_RSI_Hi():
#     stock_tick_list = []
#     stock_rsi_list = []
#     count = 0
# #     join_data = pd.DataFrame()
#     for stock in sp500_tickers:
#         stockRSI = calcRSI(stock)
#         stock_tick_list.append(stockRSI["Ticker"])
#         stock_rsi_list.append(stockRSI["RSI"])
#         count+=1
#         print(count)
#     rsi_df_hi = pd.DataFrame(data=(stock_rsi_list), index=stock_tick_list, columns=["RSI"])
#     rsi_df_hi.sort_values(by=["RSI"], ascending=False,inplace=True)

#     return rsi_df_hi


