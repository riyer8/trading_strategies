# Trading Strategies

## Manual Trading

### **Stock Tickets**

Through `stock_trading_ticket.py`, we are able to create a new ticket to trade stock at the current market price. This will store all your previous portfolio trades in a csv file `data/stock_trade_log.csv` which will contain the `Date, Ticker, Shares, Price` information for every previous trade.

We may calculate our entire portfolio calculation through `stock_portfolio_calculations.py`. This file *requires* there to be a trade executed.

### **Options Tickets**

The options tickets can be accessed at `option_trading_ticket.py` which is similar to `stock_trading_ticket.py` with the additional option of executing a call or put. There is no cost for executing a trade.

We may calculate our entire portfolio calculation through `option_portfolio_calculations.py`. This file *requires* there to be a trade executed.