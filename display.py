#!/usr/bin/env python3
#for displaying query results

from server.py import *
import pandas as pd

q1 = """
SELECT *
FROM CPUs;
"""

results = read_query(connection, q1)

from_db = []

for result in results:
  result = list(result)
  from_db.append(result)


columns = ["CPU Name", "Price", "Performance", "TDP", "iGPU", "P-Cores", "E-Cores", "Threads", "OC"]
df = pd.DataFrame(from_db, columns=columns)

display(df) #final result should display CPU table neatly on webpage
