# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:49:01 2021

@author: Rutuja Kardile
"""

import cx_Oracle
import pandas as pd


con=cx_Oracle.connect('system/123@127.0.0.1/XE')
if con!=None:
    print(con.version)
    print("connection done")

cur=con.cursor()

cur.execute("select * from patients")
table_rows = cur.fetchall()
df = pd.read_sql('SELECT * FROM patients',con=con)  # fitting into pandas dataframe
df.set_index(['CUST_ID'], inplace=True)  # setting default index
print (df)
a='IND'.ljust(5)
ans = df.loc[df['COUNTRY']==a]
print(ans)


def show_data(country):
    a=country.ljust(5)
    data = df.loc[df['COUNTRY'] == a]
    print(data)

def get_file(country):
    a=country.ljust(5)
    data = df.loc[df['COUNTRY'] == a]
    file_name = str(country)
    data.to_csv('C:/Users/kardi/downloads/' + country + ".csv")  # replace path with your desired path
    print("File has been created to the specified path")

#calling functions

show_data("IND")
get_file("IND")