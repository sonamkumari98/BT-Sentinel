import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sonam1998",
    database="my_project"
)

print("Database connected successfully")


#import pandas as pd
#import mysql.connector

#conn = mysql.connector.connect(
   # host="localhost",
   # user="root",
   # password="Sonam1998",
   # database="my_project"
##)
##query = "SELECT * FROM Employees"
##df=pd.read_sql(query, conn)

#print(df)




#Multiple tables import kro
from sqlalchemy import create_engine
import pandas as pd

# Connection string banayein (Sahi password aur DB name daalein)
# Format: mysql+mysqlconnector://user:password@host/database
engine = create_engine("mysql+mysqlconnector://root:Sonam1998@localhost/my_project")

# Ab tables read karein bina kisi warning ke
employees = pd.read_sql("SELECT * FROM Employees", engine)
projects = pd.read_sql("SELECT * FROM Projects", engine)
leaves = pd.read_sql("SELECT * FROM leaves", engine)
Timesheet = pd.read_sql("SELECT * FROM Timesheet", engine)


print(employees.head())

print()

print(projects.head())
print()


print(leaves.head())
print()

print(Timesheet.head())
print()
