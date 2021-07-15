import pymysql
import pandas as pd

# Open database connection
connection = pymysql.connect('localhost', 'user', 'password', 'uni-database')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute SQL query using execute() method.
cursor.execute('SELECT * FROM readings')

# Load the data from the database
data = cursor.fetchall()

# Pass in the column names
column_names = [cols[0] for cols in cursor.description]

# Convert data into DataFrame
df = pd.DataFrame(data, columns=column_names)
print(df.to_string())
