<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/84649228/129124128-4bab2bc5-2748-499a-818b-c9c3834b4031.png"> 
</p>


Finding new stocks to invest in can be a tedious task. From researching stocks, following the market, measuring returns, and so many other things, these tasks can take up so much of your time. Why sit behind your computer or on your phone for countless hours researching stocks, when you could be doing other things with your time. You have a whole life to live and enjoy. Don't get dragged down by these stifling tasks. Let the Quickr Pickr assist you.


<details>
<summary>Why Quickr Pickr?</summary>
With the Quickr Pickr, you don't have to worry about spending your free time searching and studying one stock at a time. This innovative application saves you time, so you can start making quality investment decisions. By choosing the criteria that suits your investing needs, you are able to find stocks faster and with ease. 
</details>

<details>
<summary>Our Motivation</summary>
Our goal is to give the user an efficient and informative experience. Investing takes research and practice in making well informed decisions about the stock market. We wanted to deliver an experience where it does not have to be difficult to be well informed. We have developed key indicators of stocks that the user can rely on. Of course we support doing research on stocks that are given to the users to give them a better idea of what they would be investing in. 
</details>


<h3 align="center"> Ultimately, Quickr Pickr wants YOU to get richer quickr. </h3>

---
  
## Technologies
This application was created using JupyterLab and VS Code, as the main language used was Pandas/Python. To be able to run this program, this must be ran using a Git Bash terminal, or VS code. 

**Systems**

[conda 4.10.3](https://docs.anaconda.com/anaconda/install/index.html) - Package manager, Environment Manager

Python 3.7 - included in Anaconda

[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) - Web-based user interface

[Pandas](https://pandas.pydata.org/) - Open source data analysis and manipulation tool

**Packages**

[Yahoo! Finance](https://pypi.org/project/yfinance/) - Provides historical market data from Yahoo! finance

[Numpy](https://numpy.org/doc/stable/) - Python library that provides multidimensional array objects, derived objects, and routines for faster operations

[Matplotlib](https://matplotlib.org/stable/users/installing.html) - Python library that provides static, animated, and interactived visualizations

[fire](https://github.com/google/python-fire) - Command line interface, help page, and entry-point

[questionary](https://github.com/tmbo/questionary) - Interactive user prompts and dialogs

---

## Installation Guide
 
<details>
<summary>Installation for Development</summary>

Below are installations for the development side of the project. If you wish to understand the code behind the application, please install the following. 

```JupyterLab
conda active dev
python -m ipykernel install --user --name dev
conda install -c conda-forge nodejs
conda deactivate

```
Once installed you should be able to open JupyterLab by the following code:

```
conda activate dev
jupyter lab
```

To exit out of JupyterLab hit: Ctrl + C

It is important to also instal Pandas as the majority of code use is using language from Pandas.

```Pandas
conda activate dev
conda install pandas -y
conda deactive
```   

</details>

<details>
<summary>Installations Needed to Run Application</summary>

Yahoo Finance

```
 pip install yfinance --upgrade --no-cache-dir
```

Numpy

```
pip install numpy
```


Matplotlib
    
```
conda install matplotlib
```


Fire
    
```
  pip install fire
```

Questionary
    
```
  pip install questionary
```

</details>

---

## Usage 


To engage the users, we wanted them to be able to select from a group of indicators that we believe will give the user the most informative decision tools.

**Indicators**
<details>
<summary> Relative Strength Index </summary>
Relative Strength Index (RSI) is a momentum indicator used to measure the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of stock or other asset. 

* High RSI values of 70 or over indicate that stock is becoming overbought or overvalued and may be primed for a trend reversal. 
* Low RSI value of 30 or below indicates an oversold or undervalued condition. 

[More Information on RSI](https://www.investopedia.com/terms/r/rsi.asp)
</details>

<details>
<summary> Simple Moving Average (50%) </summary>
Simple Moving Average (SMA) is a technical indicator that aids in determining if a stock is in a uptrend or downtrend. To calculate this, we take the average of a range of closing prices divided by the amount of periods in that range.

Our SMA50% is a 50-day moving average is calculuated by summing up the past 50 data points and then dividing the result by 50.
* High SMA50% values indicate an uptrend for the stock. 
* Low SMA50% value indicates a downtrend for the stock. 
    
[More Information on SMA](https://www.investopedia.com/terms/s/sma.asp)
    
[More Information on SMA50%](https://www.investopedia.com/ask/answers/012815/why-50-simple-moving-average-sma-so-common-traders-and-analysts.asp)
</details>

<details>
<summary> Moving Average Convergence Divergence </summary>
Moving Average Convergence Divergence(MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a stock's price. This is calculated by subtracting the 26-period exponential moving average from the 12-period exponential moving average. Exponential Moving Average (EMA) is a type of moving average that places greater weight on recent prices compared to SMA that weighs all periods equally.

* High MACD indicates that it has crossed or is greater than the signal line, meaning it is a great time to buy the stock. 
* Low MACD indicates that it has crossed or it is below the signal line, meaning it is time to sell the stock.
    
[More Information on MACD](https://www.investopedia.com/terms/m/macd.asp)
    
</details>


<details>
<summary> Moving Average Convergence Divergence-Low Divergence </summary>
Moving Average Convergence Divergence(MACD) with low divergence tells us the the MACD and signal line are close and indicate a cross will be happening soon.
    
</details>

---

## Examples



---

## Contributors

[Julia Guanzon](www.linkedin.com/in/julia-guanzon)

Saeed Raghib

[Prateek Sharma](https://www.linkedin.com/in/prateek-sharma-21a081180/)

[Sam Weiner](www.linkedin.com/in/samuel-weiner)

---

## License

GPL-3.0
