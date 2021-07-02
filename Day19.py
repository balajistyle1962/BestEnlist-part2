# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 08:52:38 2021

@author: Balaji.N.R.
"""

import xlrd
import cx_Oracle
print("BestEnlist Bootcamp python 2021\nDay19\nBalaji.N.R.")
loc=("students.xlsx")
con=cx_Oracle.connect("hr/hr@localhost")
cur=con.cursor()
print("connected to database")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print("printing the values of the excel database")
for i in range(sheet.nrows):
    print(sheet.row_values(i))
    cur.execute("create table student(stu_id number(5),stu_name varchar(10),phone number(10),mail_id varchar(20),dept varchar(5))")
print("Student Database created!")
    
rows=[]
for i in range(sheet.nrows):
    temp=sheet.row_values(i)
    rows.append(temp)
    cur.executemany("insert into student values(:1,:2,:3,:4,:5)",rows)
    con.commit()
con.close()