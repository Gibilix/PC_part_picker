#!/usr/bin/env python3
#for displaying query results

from server import create_db_connection, read_query
import pandas as pd

q1 = """
SELECT *
FROM CPUs;
"""
q2 = """
SELECT COLUMN_NAME 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME='CPUs';
"""
connection = create_db_connection("localhost", "root", "Evil-Password123", "cpu")
results = read_query(connection, q1)
from_db = []

for result in results:
  result = list(result)
  from_db.append(result)
"""
results2 = read_query(connection, q2)
columns = []

for column in results2:
  column = list(column)
  columns.append(column)
"""
df = pd.DataFrame(from_db)

print(df) #final result should display CPU table neatly on webpage