# -*- coding: utf-8 -*-
"""Quickr Pickr

This is a command line application to help investors find the stocks to invest in. 

"""
import fire
import questionary
import sys
import pandas as pd
import yfinance as yf
import datetime as dt
import numpy as np
from pathlib import Path
from termcolor import colored as cl
import matplotlib.pyplot as plt
import pprint

plt.rcParams['figure.figsize'] = (20, 10)
plt.style.use('fivethirtyeight')
from pathlib import Path
pp = pprint.PrettyPrinter(indent=4)
from utils.financial_functions import *
from utils.fileio import save_csv

def introduction():
    starter_question = questionary.select(
        "Welcome! Are you ready to use Quickr Pickr?",
        choices = [
            "YES",
            "NO"
        ]
    ).ask()

    if starter_question == "YES":
        return get_ticks()
        
    else:
        sys.exit(f"Goodbye!")

def long_or_short():
    answer = questionary.select("Would you like to see short or long term indicators?", choices=[
        "Short Term Indicators",
        "Long Term Indicators"
    ]).ask()

    return answer


def get_indicators(sp500_ticks):
    #J.Guanzon Comment: Next questionary will ask if the user would like to download the most recent momentum data.
    # If they choose yes, the program will run functions to gather the data. If no, they will be prompted to the next question.
    recent_momentum_data = questionary.select(
        "Would you like to download our most recent momentum data? This may take a few minutes to download.",
        choices = [
            "YES",
            "NO"
        ]
    ).ask()

    if recent_momentum_data == "YES":
        return todays_indicators(sp500_ticks)
    elif recent_momentum_data == "NO":
        ask_again =questionary.select(
            "Are you sure?",
            choices= [
                "YES",
                "NO"
            ]
        ).ask()
    if ask_again == "YES":
        sys.exit(f"Goodbye!")
    else:
        return todays_indicators(sp500_ticks)

def get_long_indicators(sp500_ticks):
    recent_long_data = questionary.select(
        "Would you like to download our most recent long term data? This will take a while to download.",
        choices = [
            "YES",
            "NO"
        ]
    ).ask()

    if recent_long_data == "YES":
        return get_longterm(sp500_ticks)
    elif recent_long_data == "NO":
        ask_again =questionary.select(
            "Are you sure?",
            choices= [
                "YES",
                "NO"
            ]
        ).ask()
    if ask_again == "YES":
        sys.exit(f"Goodbye!")
    else:
        return get_longterm(sp500_ticks)

def choose_indicator():
    answer = questionary.select(
    "What indicator would you like to sort the S&P 500 by?",
    choices= [
        "High RSI",
        "Low RSI",
        "High MACD",
        "Low MACD",
        "High SMA50%",
        "Low SMA50%",
        "Low MACD Divergence"
    ]  
    ).ask()

    return answer

def choose_long_indicator():
    answer = questionary.select("What indicator would you like to sort the S&P 500 by?",
    choices=[
        "High Total Debt",
        "Low Total Debt",
        "High Debt to Equity",
        "Low Debt to Equity",
        "Market Cap",
        "Forward P/E"
    ]).ask()

    return answer

def sort_by_indicator(df, indicator):
    sorted_df = sort_indicators(df, indicator)

    return sorted_df

def sort_by_long_indicator(df, indicator):
    sorted_long_df = sort_longterm(df, indicator)

    return sorted_long_df

def chart_or_info_q(ticker_list):
    answer = questionary.select(
        "Would you like to see the chart for or additional information about a particular stock?",
        choices=[
            "Chart",
            "Info",
            "Neither"
        ]
    ).ask()
    if answer == "Chart":
        ticker = questionary.text("Please input the ticker you'd like to see a chart of").ask().upper()
        if ticker in  ticker_list:
            chart = get_chart(ticker)
            return chart
        else:
            print("The ticker you entered namely '" + ticker + "' is not in the SP500.")
            return chart_or_info_q(ticker_list)
    elif answer == "Info":
        ticker = questionary.text("Please input the ticker you'd like to see a more info on").ask().upper()
        # Saeed: Adding ERROR checking
        if ticker in  ticker_list:
            info = get_info(ticker)
            return info
        else:
            print("The ticker you entered namely '" + ticker + "' is not in the SP500.")
            return chart_or_info_q(ticker_list)
    else:
        last_chance = questionary.select(
            "Are you sure you want to exit the application?",
            choices= [
                "YES",
                "NO"
            ]
        ).ask()
        if last_chance == "YES":
            sys.exit(f"Thank you for using Quickr Pickr! See you soon!")
        else:
            return chart_or_info_q(ticker_list)
    

def run():

    # Introductory Question
    sp500_ticks = introduction()
    # print(sp500_ticks)

    # User decides between short and long term
    answer = long_or_short()
    if answer == "Short Term Indicators":

        # Build the indicator DataFrame
        test_list = ["AAPL", "WMT", "GOOG"] #SW: Test list for speed of testing, will be sp500_ticks
        today_df = get_indicators(test_list) #SW: get_indicators will use (sp500_ticks) in final build

        print(today_df)

        # Let user choose Indicator
        indicator = choose_indicator()

        # Sort by chosen indicator
        sorted_list = sort_by_indicator(today_df, indicator)
        sorted_list_head = sorted_list.head(2) #SW: Thinking of adding an option to choose how many results you'd like.
        print(sorted_list_head)

    else:
        test_list = ["AAPL", "GOOG", "WMT"] #SW: Just a test list, this will be sp500_ticks
        df = get_long_indicators(test_list) # SW: Will use (sp500_ticks)

        print(df)

        # Let user choose indicator
        long_indicator = choose_long_indicator()

        # Sort by chosen indicator
        sorted_long = sort_by_long_indicator(df, long_indicator)
        sorted_long_head = sorted_long.head(2)
        print(sorted_long_head)

        #
    # Check to see if the user would like a chart or more info on a specific stock.
    result = chart_or_info_q(test_list) #SW: Will be sp500_ticks
    pp.pprint(result)

# SW: I'd like to figure out a "main loop" for iteration number 2

if __name__ == "__main__":
    fire.Fire(run)