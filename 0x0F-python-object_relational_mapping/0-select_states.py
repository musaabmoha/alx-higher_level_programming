#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#<mysql password> \
#<database name>
import MySQLdb
from sys import argv

'''
a script that lists all states
from the database
'''
if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()

