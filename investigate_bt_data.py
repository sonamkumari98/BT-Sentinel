import pandas as pd
from sqlalchemy import create_engine

# Load the generated CSV data

try:
    df = pd.read_csv("bt_system_logs.csv")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # Ensure Timestamp is in datetime format
    print("--- BT-Sentinel: Investigation Started ---\n")

except FileNotFoundError:
    print("Error: CSV file not found. Please run bt_csv_data.py to generate the data first.")
    exit()

