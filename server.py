#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error
import pandas as pd
from queries.py import create_CPU_table, insert_CPU

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

connection = create_db_connection("local ip", "user", "psw", "db")
execute_query(connection, create_CPU_table)
execute_query(connection, insert_CPU)
<<<<<<< HEAD
=======

results = read_query(connection, q1)

from_db = []

for result in results:
  result = list(result)
  from_db.append(result)


columns = ["CPU Name", "Price", "Performance", "TDP", "iGPU", "P-Cores", "E-Cores", "Threads", "OC"]
df = pd.DataFrame(from_db, columns=columns)

display(df) #final result should display CPU table neatly on webpage
>>>>>>> origin
