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
    data = yf.download(ticker, period="6mo")
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

    ax1.plot(df.Close) #SW: Maybe add SMA50, also figure out y labels
    ax2.plot(df.MACD, color = 'black', linewidth = 1.5, label = 'MACD')
    ax2.plot(df.Signal, color = 'violet', linewidth = 1.5, label = 'SIGNAL')
# Plots the bar graph on within the second plot, showing different colors for positive and negative values
    for i in range(len(df.Close)):
        if str(df.HIST[i])[0] == '-':
            ax2.bar(df.Close.index[i], df.HIST[i], color = 'red')
        else:
            ax2.bar(df.Close.index[i], df.HIST[i], color = 'green')

    plt.legend(loc = 'lower right')
    plt.title(f"{ticker} Price and MACD, Last 6 Months")
    return plt.show()

# %%
# Uses calc_indicators to get Today's Values for S&P 500
def todays_indicators(stock_list):
# Create Empty lists our desired values will end up in
    stock_tick_list = []
    price_list = []
    stock_rsi_list = []
    # macd_list = []
    # sig_list = []
    hist_list = []
    sma_pct = []
#   Saeed
    dept_to_equity = []
    total_debt = []
    market_cap = []
#    total_revenue = []


# Add a count so the user can know how far along they are   
    count = 0
# Iterate through the S&P 500, appending each list with the appropriate value for the most recent close
    for stock in stock_list:
        stock_indicators = calc_indicators(stock)
        today = stock_indicators.iloc[-1]
        stock_tick_list.append(today["Ticker"])
        price_list.append(today["Close"])
        stock_rsi_list.append(today["RSI"])
        # macd_list.append(today["MACD"])
        # sig_list.append(today["Signal"])
        hist_list.append(today["HIST"])
        sma_pct.append(today["SMA50%"])
    # Saeed
        info_all = yf.Ticker(stock).info                # Read in the information

        dept_to_equity.append(info_all['debtToEquity'])
        total_debt.append(info_all['totalDebt'])
        market_cap.append(info_all['marketCap'])
#        total_revenue.append(info_all['totalRevenue'])

        count+=1
        print(count)

    frames = {"Price" : price_list,
            "RSI" : stock_rsi_list,
            #  "MACD": macd_list,
            #  "Signal": sig_list,
             "HIST" : hist_list,
             "SMA50%": sma_pct,
    # Saeed
            "Debt to Equity": dept_to_equity,
            "Total Debt" : total_debt,
            "Market Cap": market_cap#,
#            "Total Revenue": total_revenue
             }
    today_df = pd.DataFrame(data=frames, index=stock_tick_list)
    today_df = today_df.rename(columns={"HIST" : "MACD_Strength"})
    
    return today_df


# %%
# Sorts today_df by the indicator chosen by questionary. todays_calculations must be saved into today_df!
def sort_indicators(today_df, indicator):
    if indicator == "High RSI":
        today_df.sort_values(by=["RSI"], ascending=False,inplace=True)
    elif indicator == "Low RSI":
        today_df.sort_values(by=["RSI"], ascending=True,inplace=True)
    elif indicator == "High MACD":
        today_df.sort_values(by=["MACD_Strength"], ascending=False, inplace=True)
    elif indicator == "Low MACD":
        today_df.sort_values(by=["MACD_Strength"], ascending=True, inplace=True)
    elif indicator == "High SMA50%":
        today_df.sort_values(by=["SMA50%"], ascending=False, inplace=True)
    elif indicator == "Low SMA50%":
        today_df.sort_values(by=["SMA50%"], ascending=True, inplace=True)
    elif indicator == "Low MACD Divergence":
        divergence = [abs(i) for (i) in today_df.MACD_Strength]
        today_df["Divergence"] = divergence
        today_df.sort_values(by=["Divergence"], ascending=True, inplace=True)
# Saeed - only adding 4 indicator out of 6
    elif indicator == "Debt to Equity":
        today_df.sort_values(by=["Debt to Equity"], ascending=True, inplace=True)
    elif indicator == "Total Debt":
        today_df.sort_values(by=["Total Debt"], ascending=True, inplace=True)
    elif indicator == "Market Cap":
        today_df.sort_values(by=["Market Cap"], ascending=False, inplace=True)
    # elif indicator.sort_values(by=["Total Revenue"]):
    #     today_df.sort_values(by=["Total Revenue"], ascending=False, inplace=True)
        
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


