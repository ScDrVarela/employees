"""

The following script will open and close (uncommenting last code line) a connection to a specific database

"""

#For the connection we are to use environment variables

import os
sqluser = os.environ.get('sqluser')
sqlpass = os.environ.get('sqlpass')

# First we import the mysql.connector module
import mysql.connector
"""

The very first time I tried to import the module it pop out the following error message:

ImportError: No module named mysql.connector

The solution python pip install mysql-connector-python-rf didn't solve this.
It was solved by installing mySQL module as well as mysql-connector in the Python Packages section below

"""

"""
Pandas:
We will be using the Pandas module to retrieve data from a csv file.
The data we will be retrieving is the db name

"""

import pandas as pd
db = pd.read_csv("db_names.csv")
dbfe = list(db.columns)[0]

# Then we set a new variable to connect to the database
connection1 = mysql.connector.connect(user=sqluser, password=sqlpass,
                                      host='127.0.0.1',
                                      database=dbfe)

"""To verify if the connection with the SQL database was successful, uncomment the following line (remove the #):

#print(connection1)

This must show something like:
<mysql.connector.connection_cext.CMySQLConnection object at 0x00000160B03A53D0>

"""
print(connection1)
# Finally, we can close the connection with variable.close(), just uncomment
connection1.close()

#If you get the error message about connection not stablished, try to restart the IDE for it to save
#the environment variables.