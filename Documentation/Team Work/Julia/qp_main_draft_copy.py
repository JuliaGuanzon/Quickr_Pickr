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


plt.rcParams['figure.figsize'] = (20, 10)
plt.style.use('fivethirtyeight')
from pathlib import Path

from utils.financial_functions import *
from utils.fileio import save_csv

#J.Guanzon Comment: The questionary below will greet the user and ask if they would like to use the program.
# If they choose yes, the program will run get_ticks which calls the S&P 500 data. If they choose no, they will be exited out the program.
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

def sort_by_indicator(df, indicator):
    sorted_df = sort_indicators(df, indicator)

    return sorted_df

def chart_or_info_q():
    answer = questionary.select(
        "Would you like to see the chart for or additional information about a particular stock?",
        choices=[
            "Chart",
            "Info",
            "Neither"
        ]
    ).ask()
    if answer == "Chart":
        ticker = questionary.text("Please input the ticker you'd like to see a chart of").ask()
        chart = get_chart(ticker)

        return chart
    
    elif answer == "Info":
        ticker = questionary.text("Please input the ticker you'd like to see a more info on").ask()
        info = get_info(ticker)

        return info
    
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
            return chart_or_info_q()
            


def run():

    # Introductory Question
    sp500_ticks = introduction()
    # print(sp500_ticks)

    # Build the indicator DataFrame
    test_list = ["AAPL", "WMT", "GOOG"] #SW: Test list for speed of testing, will be sp500_ticks
    today_df = get_indicators(test_list) #SW: get_indicators will use (sp500_list) in final build

    print(today_df)

    # Let user choose Indicator
    indicator = choose_indicator()

    # Sort by chosen indicator
    sorted_list = sort_by_indicator(today_df, indicator)
    sorted_list_head = sorted_list.head(2) #SW: Thinking of adding an option to choose how many results you'd like.
    print(sorted_list_head)

    # Check to see if the user would like a chart or more info on a specific stock.
    result = chart_or_info_q()
    print(result)

    save_stock_picks(result)

def save_stock_picks(result):
    """Saves the qualifying stocks to a CSV file.

    Args:
        qualifying_stocks (list of lists): The qualifying stocks.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # J.Guanzon Comment- Used questionary.confirm to prompt a "yes/no" response. By saying "y" to the prompt, the user can save the file, and the program will advise the location of the file.
    csvpath = questionary.confirm("Would you like to save these picks?").ask()
    csvpath = Path('./top_picks/stockpicks.csv')
    save_csv(csvpath,result)
    print (f"The file is located here: {csvpath}.")


if __name__ == "__main__":
    fire.Fire(run)