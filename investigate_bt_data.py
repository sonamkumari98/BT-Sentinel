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




#---REPORT GENERATION---
print(f" FOUND{len(unauthorized_changes)} UNAUTHORIZED CONFIG CHANGES:")

if not unauthorized_changes.empty: 
    print(unauthorized_changes[['Timestamp', 'User_ID', 'System_Name']].head())

    print(f"\n BRUTEFORCE SUSPECTS (Multiple Failed Logins):")
    print(bruteforce_suspects if not bruteforce_suspects.empty else "None")
    print(f"\n SUSPICIOUS NIGHT LOGINS DETECTED: {len(night_logins)}")

    print(f"\n NIGHT LOGINS (12 AM - 5 AM):")
    print(night_logins[['Timestamp', 'User_ID', 'IP_Address']].head() if not night_logins.empty else "None")
else:
    print("No Unauthorized Changes Found")


#4. Export for Stakeholders (Power BI / Excel)
# We will create a cleaned 'Alert Report' that we can import into Power BI.
unauthorized_changes.to_csv('bt_alerts_report.csv', index=False)
print("\n Investigation Report saved as 'bt_alerts_report.csv' for Power BI.")


#1. SQL Engine banayein

# Password ki jagah apna MySQL password likhein (Example: 'root123')

engine = create_engine('mysql+mysqlconnector://root:Sonam1998@localhost/bt_sentinel_db')


#2. DataFrame(df) ko direct SQL Table mein upload karein
#"replace" ka matlab hai har bar naya data purane data ko update kar dega.
df.to_sql('bt_system_logs', con=engine, if_exists='replace', index=False)
print("\n Success: Data Python se MySQL Database mein chala gaya hai!")

