# Trading Strategies

## Manual Trading

### **Stock Trading**

#### **stock_trading_ticket.py**

This script provides a graphical user interface (GUI) to submit stock trades. It allows users to enter a ticker symbol and the number of shares they wish to trade. Upon submission, the script retrieves the current market price for the specified stock and logs the trade into `data/stock_trade_log.csv`, which records the trade details including the date, ticker, number of shares, and price.

#### **stock_portfolio_calculations.py**

This script calculates and displays the current value of your stock portfolio. It reads from `data/stock_trade_log.csv`, retrieves the latest stock prices, and computes the total portfolio value and the gain or loss for each stock.

### **Options Trading**

#### **option_trading_ticket.py**

This script provides a GUI for submitting options trades, allowing users to specify the ticker symbol, number of shares, and whether the option is a call or put. It logs this information into `data/options_trade_log.csv`, which includes the date, ticker, number of shares, price bought, and type of option.

#### **option_portfolio_calculations.py**

This script calculates the value of your options portfolio. It reads from `data/options_trade_log.csv`, retrieves the latest prices, and computes the value of call and put options. It also provides a summary of gains or losses for each option.

## Future Enhancements

Plans are in place to integrate automated trading strategies to further enhance the trading experience.
