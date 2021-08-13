# -*- coding: utf-8 -*-
"""Quickr Pickr

This is a command line application to help investors find the stocks to invest in. 
This is a rough draft, until we know what our variables are then we can start to test.
We will have to use utils and filters on separate files and pull them into this or our main file.
Copied the format from a previous activity in Mod2.

I will keep fiddling with the if-else statements. I am having a problem executing the questionary.select, but in the documentation for questionary it should work.

Example:
    $ python app.py
"""
import sys
import fire
import questionary
from pathlib import Path


def get_user_information():
    """Ask the user for their risk tolerance

    By asking how much risk they want to take on, we can build around the RSI and the moving avg data to make sure they get what they ask for. 

    """
    risk_tolerance = questionary.select(
        "How much risk are you willing to take on?"
        choices = [
            "I'm willing to take on a risk",
            "I'm indifferent to risk",
            "I'm risk adverse"
        ]
    ).ask()

    if risk_tolerance ==  "I'm willing to take on a risk":
        rsi > 70
        moving_avg_200days <0%
    elif risk_tolerance == "I'm risk adverse":
        rsi < 30
        moving_avg_200days > 50%
    else:
        rsi 
        moving_avg_200

    print(f"You have have chosen {risk_tolerance} ")
    
#Not sure what to code for this just yet
    stock_volume = questionary.select().ask()

#Not sure what to code for this just yet
    stock_price = questionary.text(
        "How much are you willing to pay for a stock"
    ).ask()

    stock_price = float(stock_price)


    return risk_tolerance, stock_volume, stock_price
 
    # sectors = questionary.select(
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

def find_qualifying_stocks(risk_tolerance, stock_volume, stock_price):
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

 
    stock_data_filtered = filter_rsi(risk_tolerance, X)
    stock_data_filtered = filter_moving_avg_200days(risk_tolerance, X)
    stock_data_filtered = filter_volume(stock_volume, X)
    stock_data_filtered = filter_price(stock_price, X)

    print(f"Found {len(stock_data_filtered)} qualifying stocks")

    return stock_data_filtered




def run():
    """The main function for running the script."""

    # Load the latest Bank data
    stock_data = load_stock_data()

    # Get the applicant's information
    risk_tolerance, stock_volume, stock_price = get_user_information()

    # Find qualifying loans
    qualifying_stocks= find_qualifying_stocks(
        stock_data, risk_tolerance, stock_volume, stock_price
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
    header = ["Ticker", "Open", "High", "Low", "Close", "Adj Cose","Volume", "Moving Avg 200 Days","Price Change","Gains","Avg UP"]
    save_csv(csvpath, qualifying_stocks, header)
    print (f"The file is located here: {csvpath}.")
   