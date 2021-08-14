
import questionary


rsi_indicator = questionary.select(
        "Regarding relative strength index, what are you looking for?",
        choices = [
            "I'm looking for an RSI of 70 or greater",
            "I'm looking for an RSI between 30 and 70",
            "I'm looking for an RSI of 30 or less"
        ]
    ).ask()

volume_indicator = questionary.select(
        "Are you intersted in stocks that have high or low volume?",
        choices = [
            "High Volume",
            "Low Volume"
        ]
    ).ask()

price_indicator = questionary.select(
        "How much are you willing to pay?",
        choices = [
            "I want to spend less than $100 on one stock",
            "I want to spend less than $1000 on one stock",
            "I do not have a limit"
        ]
    ).ask()
