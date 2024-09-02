import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import pandas as pd
from datetime import datetime
import warnings
import os

warnings.filterwarnings("ignore", category=FutureWarning, module="yfinance")
warnings.filterwarnings("ignore", category=FutureWarning, module="pandas")

def initialize_options_log():
    if not os.path.exists('data/options_trade_log.csv'):
        df = pd.DataFrame(columns=['Date', 'Ticker', 'Shares', 'Price Bought', 'Call/Put'])
        df.to_csv('data/options_trade_log.csv', index=False)

def submit_options_trade():
    ticker = entry_ticker.get().upper()

    try:
        shares = int(entry_shares.get().strip())
    except ValueError:
        messagebox.showerror("Share Error", "Please enter a valid number of shares.")
        return
    
    option_type = option_var.get()

    if option_type not in ["Call", "Put"]:
        messagebox.showerror("Option Type Error", "Please select either a Call or Put option.")
        return

    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[0]
    except IndexError:
        messagebox.showerror("Ticker Error", "Ticker not found. Please enter a valid ticker symbol.")
        return
    
    options_log = pd.read_csv('data/options_trade_log.csv')
    new_trade = pd.DataFrame({
        'Date': [datetime.now()], 
        'Ticker': [ticker], 
        'Shares': [shares], 
        'Price Bought': [price], 
        'Call/Put': [option_type]
    })
    
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=FutureWarning, message=".*DataFrame concatenation with empty or all-NA entries.*")
        options_log = pd.concat([options_log, new_trade], ignore_index=True)
    
    options_log.to_csv('data/options_trade_log.csv', index=False)

    messagebox.showinfo("Trade Submitted", f"Trade Submitted: {ticker} {shares} shares at ${price:.2f} per share, {option_type} option")

root = tk.Tk()
root.title("Options Trade Ticket")
initialize_options_log()

label_ticker = tk.Label(root, text="Ticker Symbol:")
label_ticker.grid(row=0, column=0, padx=10, pady=10)
entry_ticker = tk.Entry(root)
entry_ticker.grid(row=0, column=1, padx=10, pady=10)

# Negative shares indicate selling
label_shares = tk.Label(root, text="Number of Shares:")
label_shares.grid(row=1, column=0, padx=10, pady=10)
entry_shares = tk.Entry(root)
entry_shares.grid(row=1, column=1, padx=10, pady=10)

# Default selection to "Call"
option_var = tk.StringVar(value="Call")
radio_call = tk.Radiobutton(root, text="Call", variable=option_var, value="Call")
radio_call.grid(row=2, column=0, padx=10, pady=10)
radio_put = tk.Radiobutton(root, text="Put", variable=option_var, value="Put")
radio_put.grid(row=2, column=1, padx=10, pady=10)

button_submit = tk.Button(root, text="Submit Trade", command=submit_options_trade)
button_submit.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()