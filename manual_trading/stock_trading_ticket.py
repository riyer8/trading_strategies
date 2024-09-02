import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import pandas as pd
from datetime import datetime
import warnings
import os

warnings.filterwarnings("ignore", category=FutureWarning, module="yfinance")
warnings.filterwarnings("ignore", category=FutureWarning, module="pandas")

def initialize_trade_log():
    if not os.path.exists('data/stock_trade_log.csv'):
        df = pd.DataFrame(columns=['Date', 'Ticker', 'Shares', 'Price'])
        df.to_csv('data/stock_trade_log.csv', index=False)

def submit_trade():
    ticker = entry_ticker.get().upper()
    try:
        shares = int(entry_shares.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of shares.")
        return

    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'][0]
    except IndexError:
        messagebox.showerror("Ticker Error", "Ticker not found. Please enter a valid ticker symbol.")
        return
    
    trade_log = pd.read_csv('data/stock_trade_log.csv')
    new_trade = pd.DataFrame({
        'Date': [datetime.now()], 
        'Ticker': [ticker], 
        'Shares': [shares], 
        'Price': [price]
    })
    
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=FutureWarning, message=".*DataFrame concatenation with empty or all-NA entries.*")
        trade_log = pd.concat([trade_log, new_trade], ignore_index=True)
    
    trade_log.to_csv('data/stock_trade_log.csv', index=False)

    messagebox.showinfo("Trade Submitted", f"Trade Submitted: {ticker} {shares} shares at ${price:.2f} per share")

root = tk.Tk()
root.title("Submit Trade Ticket")

initialize_trade_log()

label_ticker = tk.Label(root, text="Ticker Symbol:")
label_ticker.grid(row=0, column=0, padx=10, pady=10)
entry_ticker = tk.Entry(root)
entry_ticker.grid(row=0, column=1, padx=10, pady=10)

label_shares = tk.Label(root, text="Number of Shares:")
label_shares.grid(row=1, column=0, padx=10, pady=10)
entry_shares = tk.Entry(root)
entry_shares.grid(row=1, column=1, padx=10, pady=10)

button_submit = tk.Button(root, text="Submit Trade", command=submit_trade)
button_submit.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()