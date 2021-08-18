# -*- coding: utf-8 -*-
"""Quickr Pickr

This is a command line application to help investors find the stocks to invest in. 

"""
import fire
import questionary
from pathlib import Path

from utils.financial_functions import calc_indicators
from utils.fileio import save_csv
# load_csv,

# from qualifier.utils.calculators import (
#     calculate_monthly_debt_ratio,
#     calculate_loan_to_value_ratio,
# )s

# from qualifier.filters.max_loan_size import filter_max_loan_size
# from qualifier.filters.credit_score import filter_credit_score
# from qualifier.filters.debt_to_income import filter_debt_to_income
# from qualifier.filters.loan_to_value import filter_loan_to_value


# def load_bank_data():
#     """Ask for the file path to the latest banking data and load the CSV file.

#     Returns:
#         The bank data from the data rate sheet CSV file.
#     """

#     csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
#     csvpath = Path(csvpath)
#     if not csvpath.exists():
#         sys.exit(f"Oops! Can't find this path: {csvpath}")

#     return load_csv(csvpath)


def get_user_information():
    """Ask the user a series of questions.

    By asking these questions, we can build a list of stocks that match their criteria.
    """
    #J.Guanzon Comment: RSI
    rsi_indicator = questionary.select(
        "Regarding relative strength index, what are you looking for?",
        choices = [
            "I'm looking for an RSI of 51 or greater",
            "I'm looking for an RSI of 50 or less"
        ]
    ).ask()

    if rsi_indicator == "I'm looking for an RSI of 51 or greater":
        rsi_indicator = data["RSI"].apply(lambda x: x if x >= 51)
    
    else:
        rsi_indicator = data["RSI"].apply(lambda x: x if x <= 50)

    #J.Guanzon Comment: Volume
    sma50_indicator = questionary.select(
        "Are you intersted in stocks that have high or low volume?",
        choices = [
            "High Volume",
            "Low Volume"
        ]
    ).ask()

    if sma50_indicator == "High Volume":
        sma50_indicator = data["Volume"].apply(lambda x: x if x >= 1001)
    
    else:
        sma50_indicator = data["Volume"].apply(lambda x: x if x <= 1000)

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

    # J.Guanzon Comment: Moving Average
    # moving_avg_indicator = questionary.select(
    #     "How much historical data would you like to base your information off of?",
    #     choices = [
    #         "One year",
    #         "One month"
    #     ]
    # ).ask()

    # if moving_avg_indicator == "I want to spend less than $1000 on one stock":
    #     moving_avg_indicator = data["Moving Average"].apply(lambda x: x if x = 12mo)

    # else:
    #     moving_avg_indicator = data["Moving Average"].apply(lambda x: x if x <= 1mo)

    # sector_indicator = questionary.select(
    #     "What type of sector are you interested in investing in?",
    #     choices = [
    #         "Information Technology",
    #         "Energy",
    #         "Materials",
    #         "Industrials",
    #         "Utilities",
    #         "Healthcare",
    #         "Financials",
    #         "Consumer Discretionary",
    #         "Consumer Staples",
    #         "Communication Services",
    #         "Real Estate"]
    # ).ask()

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