# src/data_loader.py
import pandas as pd
import numpy as np
import os

def load_brent_data(filepath: str) -> pd.DataFrame:
    """
    Loads Brent crude oil prices dataset, converts Date to datetime,
    and returns a cleaned DataFrame sorted by date.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
        
    df = pd.read_csv(filepath)
    # Flexible parsing to handle 'day-month-year' (e.g., 20-May-87)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    df.set_index('Date', inplace=True)
    
    # Ensure Price column is numeric
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df = df.dropna(subset=['Price'])
    return df

def calculate_log_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates log returns to convert non-stationary price series 
    into a more stationary representation for volatility analysis.
    """
    df['Log_Returns'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
    return df.dropna()