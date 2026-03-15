import pandas as pd
import random
from datetime import datetime, timedelta 

# Setting
num_records = 1000
OUTPUT_FILE = "bt_system_logs.csv"


#Sample data pool
users =["admin_vk","skumar_it","rsharam_hr","jdoe_dev","akhan_ops","System_Automate"]
ips = [f'10.192.{random.randint(10,250)}.{random.randint(10,250)}' for _ in range (20)] 
actions = ["LOGIN","LOGOUT","FILE_ACCESS","CONFIG_CHANGE","PASSWORD_RESET","DB_QUERY"]
systems = ["windows_server_UIC","Linux_Nix_Gateway","BT_Application_Server"]  
Statuses = ["SUCCESS","SUCCESS","SUCCESS","SUCCESS","ERROR"]  # Mosty success


#Start creating data
data = []
start_date = datetime.now() - timedelta(days=7)  # create logs for last 7 days

for _ in range(num_records):
    user = random.choice(users)
    ip = random.choice(ips)
    action = random.choice(actions)
    system = random.choice(systems)
    status = random.choice(Statuses)

    #Generate a random timestamp within the last 7 days
    rabdom_days = random.randint(0, 7)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    timestamp = start_date + timedelta(days=rabdom_days, hours=random_hours, minutes=random_minutes)

    
    #ITIL Integration: Add a change Ticket ID only for configration changes
    change_ticket = "N/A"
    if action == "CONFIG_CHANGE":
        if random.random() > 0.5: # 70% of changes have tickets(Good), 30% don't (Anomalies)
            change_ticket = f"CHG{random.randint(10000,99999)}"
        else:
            change_ticket = " No_Ticket_Found"  # This is our anomaly for ITIL process

            #Special anomalies for investigation
            #Anomaly 1: Night Shift Logins for HR (User "rsharam_hr" mostly works day)
    if user == "rsharam_hr" and (timestamp.hour < 8 or timestamp.hour > 18) and action == "LOGIN":
         status = "SUCCESS"  # Successful night login for an HR person? Suspicious, needs investigation
         ip = " 99.99.99.99" #Unsual I for HR

    # Anomaly 2: Multiple failed logins for "jdoe_dev"
    if user == "jdoe_dev" and _%5 == 0: #Every 5th record for this user will fail 
        action = "LOGIN"
        status = "ERROR"  # Failed login attempt for a developer, could indicate a brute-force attack
    data.append([timestamp, user, ip, action, status, system, change_ticket]) # Append the generated log entry to our data list


# Create DataFrame
columns = ["Timestamp","User_ID","IP_Address","Action","Status","System_Name","Service_Change_Ticket"] 
df = pd.DataFrame(data, columns=columns)


#Sort by timestamp for realism
df = df.sort_values(by = "Timestamp")


# Save to CSV
df.to_csv(OUTPUT_FILE, index=False)

print(f"Successfully generated {num_records} logs in {OUTPUT_FILE}")
      

