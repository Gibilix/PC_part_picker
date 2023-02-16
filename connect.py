#!/usr/bin/env python3

from server import *
from queries import create_CPU_table, insert_CPU

connection = create_db_connection("localhost", "root", "Evil-Password123", "cpu")
execute_query(connection, create_CPU_table)
for row in insert_CPU:
    execute_query(connection, row)