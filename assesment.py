# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:49:01 2021

@author: Kardile
"""

import cx_Oracle
con=cx_Oracle.connect('system/123@127.0.0.1/XE')
if con!=None:
    print(con.version)
    print("connection done")

cur=con.cursor()

cur.execute("select * from patients")
for row in cur.fetchall():
    print(row)
#table_rows = cur.fetchall()