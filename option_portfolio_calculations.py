import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def calculate_options_portfolio_value():
    try:
        options_log = pd.read_csv('data/options_trade_log.csv')
    except FileNotFoundError:
        messagebox.showerror("Error", "Options trade log file not found. Please submit some options trades first.")
        return

    tickers = options_log['Ticker'].unique()
    
    total_value = 0
    total_gain_loss = 0
    portfolio_summary = ""

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")['Close'].iloc[0]
        trades = options_log[options_log['Ticker'] == ticker]
        
        gain_loss = 0
        for _, trade in trades.iterrows():
            option_type = trade['Type']
            bought_price = trade['Price']
            shares = trade['Shares']
            
            if option_type == "Call":
                gain_loss += (current_price - bought_price) * shares
                value = max(current_price - bought_price, 0) * shares
            elif option_type == "Put":
                gain_loss += (bought_price - current_price) * shares
                value = max(bought_price - current_price, 0) * shares
            
            total_value += value
            
        total_gain_loss += gain_loss
        
        portfolio_summary += (
            f"{ticker} ({option_type}): {shares} contracts\n"
            f"Bought at ${bought_price:.2f} per share, Current Price: ${current_price:.2f}\n"
            f"Gain/Loss: ${gain_loss:.2f}\n\n"
        )

    portfolio_summary += (
        f"Total Options Portfolio Value: ${total_value:.2f}\n"
        f"Total Gain/Loss: ${total_gain_loss:.2f}"
    )
    messagebox.showinfo("Options Portfolio Value", portfolio_summary)

root = tk.Tk()
root.title("Calculate Options Portfolio Value")

button_value = tk.Button(root, text="Calculate Portfolio Value", command=calculate_options_portfolio_value)
button_value.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()