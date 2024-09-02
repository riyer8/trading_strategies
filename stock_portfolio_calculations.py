import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def calculate_portfolio_value():
    try:
        trade_log = pd.read_csv('data/stock_trade_log.csv')
    except FileNotFoundError:
        messagebox.showerror("Error", "Trade log file not found. Please submit some trades first.")
        return

    tickers = trade_log['Ticker'].unique()
    
    total_value = 0
    total_gain_loss = 0
    portfolio_summary = ""

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")['Close'][0]
        trades = trade_log[trade_log['Ticker'] == ticker]
        
        total_shares = trades['Shares'].sum()
        total_value += total_shares * current_price
        
        gain_loss = 0
        
        for _, trade in trades.iterrows():
            bought_price = trade['Price']
            shares = trade['Shares']
            gain_loss += (current_price - bought_price) * shares
        
        total_gain_loss += gain_loss
        
        portfolio_summary += (
            f"{ticker}: {total_shares} shares\n"
            f"Bought at ${bought_price:.2f} per share, Current Price: ${current_price:.2f}\n"
            f"Gain/Loss: ${gain_loss:.2f}\n\n"
        )

    portfolio_summary += (
        f"Total Portfolio Value: ${total_value:.2f}\n"
        f"Total Gain/Loss: ${total_gain_loss:.2f}"
    )
    messagebox.showinfo("Portfolio Value", portfolio_summary)

root = tk.Tk()
root.title("Calculate Portfolio Value")

button_value = tk.Button(root, text="Calculate Portfolio Value", command=calculate_portfolio_value)
button_value.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()