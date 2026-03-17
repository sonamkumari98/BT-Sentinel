🛠️ Tech Stack
Programming: Python 3.x (NumPy, Pandas, SQLAlchemy)
Database: MySQL (Relational Data Storage)
Visualization: Power BI (Interactive Security Dashboard)
Domain: Identity & Access Management (IAM), ITIL Compliance, Cybersecurity
⚙️ How It Works (The Pipeline)
1. Data Generation & Extraction (NumPy)
Generated synthetic system logs simulating real-world Windows Server activity, including Timestamps, IP Addresses, User IDs, and Action types.
2. Transformation & Security Logic (Pandas)
Unauthorized Change Detection: Flagged any CONFIG_CHANGE where the Service_Change_Ticket was missing (NO_TICKET_FOUND). This aligns with ITIL Change Management standards.
Brute-Force Detection: Grouped failed login attempts; any user with >3 FAILED statuses is flagged as a security suspect.
Night-Logins Analysis: Filtered access logs between 12 AM and 5 AM to monitor unusual off-hours activity.
3. Automated Loading (SQL)
Used SQLAlchemy to create a seamless bridge between Python and MySQL.
Processed data is automatically pushed to the bt_sentinel_db database for persistent storage.
4. Professional Visualization (Power BI)
Developed a high-impact dashboard to track compliance scores, risky users, and unauthorized activity trends.
📂 Repository Structure
├── scripts/
│   ├── investigate_bt_data.py   # Main Python ETL logic
│   └── database_setup.sql       # MySQL schema and table creation
├── dashboard/
│   └── BT_Sentinel_UIC.pbix     # Power BI Dashboard file
├── data/
│   └── processed_logs.csv       # Final cleaned data for audit
└── README.md                    # Project documentation

💡 Engineering Impact
As a Computer Science Graduate, this project demonstrates my ability to:
Build a full-stack data pipeline from scratch.
Apply Cybersecurity principles to raw data.
Bridge the gap between Software Development (Python) and Data Analytics (Power BI).
How to Use:
Run investigate_bt_data.py to process raw logs and update the MySQL database.
Open BT_Sentinel_UIC.pbix in Power BI.
Click Refresh to see the latest security insights.
