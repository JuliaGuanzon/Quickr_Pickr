# -*- coding: utf-8 -*-
"""Quickr Pickr

This is a command line application to help investors find the stocks to invest in. 

"""
import fire
import questionary
from pathlib import Path

from utils.financial_functions import get_ticks, get_dates, todays_indicators, calc_indicators
from utils.fileio import save_csv



def get_user_information():
    """Ask the user a series of questions.

    By asking these questions, we can build a list of stocks that match their criteria.
    """
    #J.Guanzon Comment: The questionary below will great the user and ask if they would like to use the program.
    # If they choose yes, the program will run the tickers and the start/end dates. If they choose no, they will be exited out the program.
    starter_question = questionary.select(
        "Welcome! Are you ready to use Quickr Pickr?",
        choices = [
            "YES",
            "NO"
        ]
    ).ask()

    if starter_question == "YES":
        return get_ticks, get_dates
    else:
        print(f"Goodbye!")

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
        return todays_indicators
    

    #J.Guanzon Comment: Price
    macd_indicator = questionary.select(
        "How much are you willing to pay?",
        choices = [
            "I want to spend less than $100 on one stock",
            "I want to spend less than $1000 on one stock",
            "I do not have a limit"
        ]
    ).ask()

    if macd_indicator == "I want to spend less than $1000 on one stock":
        macd_indicator = data["Price"].apply(lambda x: x if x <= 1000)

    else:
        macd_indicator = data["Price"].apply(lambda x: x if x)


    return rsi_indicator, sma50_indicator, macd_indicator
 


def find_qualifying_stocks(stock_data, rsi_indicator, sma50_indicator, macd_indicator):
    """Determine which stocks will appeal to the user.

    Stock qualification criteria is based on:
        - RSI
        - Moving Average 200 days
        - Volume
        - Price

    Args:
        RSI (float): A list of bank data.
        Moving Average (float): The applicant's current credit score.
        volume (float): The applicant's total monthly debt payments.
        price (float): The applicant's total monthly income.
        

    Returns:
        A list of stocks meeting criteria.

    """

 
    stock_data_filtered = filter_rsi(rsi_indicator, stock_data)
    # stock_data_filtered = filter_moving_avg_200days(risk_tolerance, X)
    stock_data_filtered = filter_sma50(sma50_indicator, stock_data_filtered)
    stock_data_filtered = filter_price(macd_indicator, stock_data_filtered)

    print(f"Found {len(stock_data_filtered)} qualifying stocks")

    return stock_data_filtered




def run():
    """The main function for running the script."""

    # Load the latest Bank data
    stock_data = load_stock_data()

    # Get the applicant's information
    rsi_indicator, sma50_indicator, macd_indicator = get_user_information()

    # Find qualifying loans
    qualifying_stocks= find_qualifying_stocks(
        stock_data, rsi_indicator, sma50_indicator, macd_indicator
    )

    # Save qualifying loans
    save_stock_picks(qualifying_stocks)


def save_stock_picks(qualifying_stocks):
    """Saves the qualifying stocks to a CSV file.

    Args:
        qualifying_stocks (list of lists): The qualifying stocks.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # J.Guanzon Comment- Used questionary.confirm to prompt a "yes/no" response. By saying "y" to the prompt, the user can save the file, and the program will advise the location of the file.
    csvpath = questionary.confirm("Would you like to save these picks?").ask()
    csvpath = Path('./data/stockpicks.csv')
    save_csv(csvpath, qualifying_stocks,)
    print (f"The file is located here: {csvpath}.")
   
if __name__ == "__main__":
    fire.Fire(run)