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

To use the Quickr Pickr application, the repository will need to be cloned from GitHub and into a local repository. The application only works in the GitBash terminal. The usage of a dev environment is imperative as the user will need to install all of the systems and packages above in order to run the applicaiton.

Open the GitBash terminal and activate your dev environment by commanding:

```
conda activate dev
```
Open and run the 'quickr_pickr.py' file by commanding:

```
python quickr_pickr.py
```
This will activate the application for the user to start finding stocks.


In order to make this application work we had to import the following:

![image](https://user-images.githubusercontent.com/84649228/130191404-8eb54803-49e2-4c08-bf03-278004f0e6e6.png)

The above imports consist of libraries that assist us with the analytics and function files that import the calculations we need for the indicators.

The usage of questionary to build the intake form was essential to the structure of the application as we wanted to make this a seamless application that was quick to move through and as simple as a click of a button. By engaging the users through a questionaire, we wanted them to be able to select from short-term or longterm indicators that Quickr Pickr believes will give the user the most gains.

Only one indicator can be chosen at a time when running this application. The user can choose from the following in the drop down menus:

**Short Term Indicators**
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

Our SMA50% is the percent that a stock is above or below its 50 day simple moving average
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

**Long Term Indicators**
<details>
<summary> Total Debt </summary>
Total debt is the amount of debt a stock company possess.  
    
* High Total Debt is very risky.
* Low Total Debt is not risky.

</details>

<details>
<summary> Debt to Equity </summary>
Debt to Equity is reflected by the stock company's total liabilities and shareholder equities. It reflects the ability of shareholder equity to cover all outstanding debts in the event of the businesses downturn.
    
* High Debt to Equity ratio indicates that the stock has a heightened risk.
* Low Debt to Equity indicates the stock has less risk associated with it.
 
[More information on Debt to Equity](https://www.investopedia.com/terms/d/debtequityratio.asp)
</details>

<details>
<summary> Market Capitalization </summary>
Market Capitalization (Market Cap) refers to how much a company is worth as determined by the stock market. It is the total market value of all outstanding shares.
    
[More information on Market Capitalization](https://www.investopedia.com/terms/m/marketcapitalization.asp)
    
</details>

<details>
<summary> Forward P/E </summary>
Forward Price Earnings is a ratio of price-to-earnings using forecasted earnings for the P/E calculation. 
    
[More information on Forward P/E](https://www.investopedia.com/terms/f/forwardpe.asp)    
</details>

After answering the criteria questions, the application provides the user with the ability to print a chart, gather more information about the stock, or neither. Once the user has chosen what type of information they need, the application will exit the user. The user is more than welcome to run different indicators, but they will have to reopen the application and start over.

---

## Examples
 
To use the application, the user will code the following, as seen in the image below, to access the application.
![image](https://user-images.githubusercontent.com/84649228/130187777-a82b9801-a363-4347-8452-a9251ead1592.png)

Quickr Picker welcomes the user and asks if they are ready to use the application. They can select 'YES' or 'NO'. If 'YES', the user will be given a next set of questions. If the user selects "NO" they will be exited from the application.
![image](https://user-images.githubusercontent.com/84649228/130187871-4d050af0-2291-4c1c-867d-4d486885d5fc.png)

Next, the user will select from short-term or long-term indicators.
![image](https://user-images.githubusercontent.com/84649228/130187941-77a0468e-ff0f-4648-a228-e914bc1cf908.png)

The application will run the calcualtion of the indicators in the background and the user will be able to call one indicator to sort the stocks. The user is then provided with a list of information needed to make decisions on what stocks to invest in.
![image](https://user-images.githubusercontent.com/84649228/130188715-63adbc9d-5d4a-4457-9f5c-f22a694129a2.png)

The application sorts the stocks by the indicator to provide the best stock possible to the user.
![image](https://user-images.githubusercontent.com/84649228/130283908-561167cb-06d0-4d96-ab77-03067905b04e.png)

Once the user gathers information on the sorted stocks, the user had the option to create a chart or to just be provided with one stock's information. Please note that the chart only presents graphs on price and the MACD. If the user choses information, they will be provided with entire financial summary of the stock company.
![image](https://user-images.githubusercontent.com/84649228/130188980-ff4a4421-e57a-4259-a909-7b74f2b1bac6.png)

The user will be asked to choose a stock to look into, and it must be a stock from the S&P 500. If they choose a stock outside of the S&P 500, they will be asked again to pick a stock form the S&P 500.
![image](https://user-images.githubusercontent.com/84649228/130189074-933a63ce-08f0-4104-bd6f-d087024e60f7.png)

If a chart is chosen, the user is provided a chart of which they are able to save.
![image](https://user-images.githubusercontent.com/84649228/130189113-b5f6db02-9bd1-4375-bfd0-ea97203b0c8b.png)

If information is chosen, the user will be provided with rows of data. The picture below is a snip-it of only a portion of the information provided.

![image](https://user-images.githubusercontent.com/84649228/130283473-ace8455c-19b5-4032-8f26-0241c77c9855.png)

When the user is done with using the application, the system will exit the user out of the application. Below is an example of the entire application ran in a terminal. 
![image](https://user-images.githubusercontent.com/84649228/130189144-08b7b8cd-2a13-468e-ad50-1d7b001888e3.png)

---

## Contributors

[Julia Guanzon](www.linkedin.com/in/julia-guanzon)

Saeed Raghib

[Prateek Sharma](https://www.linkedin.com/in/prateek-sharma-21a081180/)

[Sam Weiner](www.linkedin.com/in/samuel-weiner)

---

## License

GPL-3.0
