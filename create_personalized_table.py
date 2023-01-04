from __future__ import print_function

#This script will create a personalized table in a database

"""
We will create a command to allow the user to select the database he want to use to create
the table.

"""

print('Please select the database you want to use to create your table:')
print('Input 1 for Ferresteel DataBase')
print('Input 2 for Abastecedora DataBase')
print('Input 3 for Mauro DataBase')

print('Input the number for the database you will use: ')

x1 = int(input())
x2 = x1 - 1
dbfe = ''

#Import the fe db from csv file
import pandas as pd
db = pd.read_csv("db_names.csv")

#try:
if x1 == 1:
    dbfe = list(db.columns)[x2]
elif x1 == 2:
    dbfe = list(db.columns)[x2]
elif x1 == 3:
    dbfe = list(db.columns)[x2]
else:
    print('El programa se cerrará ya que escogió un número ')
    print('diferente a 1, 2 o 3.')
#exit(1)
#                except error:\
#                   print('Please select only between numbers 1, 2 or 3')

#Gather user & password data from environment variables
import os
sqluser = os.environ.get('sqluser')
sqlpass = os.environ.get('sqlpass')

import mysql.connector
from mysql.connector import errorcode

db_name = dbfe

tables = {}

tables['employees']=(
	"create table employees ("
	"id int not null auto_increment,"
    "employee_number int not null,"
	"fathers_name varchar(255) not null,"
	"mothers_name varchar(255),"
    "given_name varchar(255) not null,"
    "curp varchar(255) not null,"
    "rfc varchar(255) not null,"
    "nss int not null,"
    "marital_status varchar(255),"
    "school varchar(255),"
    "age int not null,"
    "start_date int not null,"
    "years_in_company int not null,"
    "born_date int not null,"
    "address varchar(255),"
    "phone int,"
    "e_mail varchar(255),"
    "emergency_number int,"
    "allergies varchar(255),"
    "sickness varchar(255),"
    "blood_type varchar(255),"
    "status varchar(255),"
    "hiring_date date,"
    "permanent_date date,"
    "quitting_date date,"
	"primary key (id)"
") engine=innodb")

#Now open the connection to the MySQLDB
connection1 = mysql.connector.connect(user=sqluser, password=sqlpass,
                                      host='127.0.0.1',
									  database=dbfe)
cursor = connection1.cursor()

"""
The following will a) create a db, b) use an already existing db or c) check
whether the db was already created or not

"""

def create_db(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(db_name))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(db_name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_db(cursor)
        print("Database {} created successfully.".format(db_name))
        connection1.database = db_name
    else:
        print(err)
        exit(1)

for employees in tables:
    table_description = tables[employees]
    try:
        print("Creating table {}: ".format(employees), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
connection1.close()