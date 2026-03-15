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

# --- ANOMALY 1: Unauthorized Changes (ITIL / ServiceNow Check) ---
# Check for CONFIG_CHANGE without a valid Ticket ID

unauthorized_changes = df[(df['Action'] == 'CONFIG_CHANGE') & (df['Service_Change_Ticket'].str.contains("No_Ticket"))]

unauthorized_changes.to_csv("BT_Security_Alert_Report.csv", index=False)

print("--- Alert Report Generated: BT_Security_Alert_Report.csv ---")



# ANOMALY 2: Bruteforce Attempt Detection

# Identify users with more than 3 FAILED logins

failed_logins= df [df['Status'] == 'FAILED'].groupby ('User_ID').size()

bruteforce_suspects =failed_logins [failed_logins > 3]


#--- ANOMALY 3: Unusual Working Hours (UIC Investigation)

# Detect logins between 12 AM and 5 AM (Suspicious for non-ops roles)

night_logins = df[(df['Action'] == 'LOGIN') & (df['Timestamp'].dt.hour < 5)]

