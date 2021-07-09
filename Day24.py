# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 07:03:54 2021

@author: Balaji.N.R.


"""
import json
import cx_Oracle
json_data=[
    {'name':"Balaji",'age':18,'Permanent_staff':False,'salary':55000.00,'dept_desgn':'Developer'},
     {'name':"Rubesh",'age':27,'Permanent_staff':False,'salary':66000.00,'dept_desgn':"TeamLeader"},
     {'name':"Karthik",'age':28,'Permanent_staff':True,'salary':78000.00,'dept_desgn':'HR'},]
res = json.dumps(json_data)

db = cx_Oracle.connect('hr/hr@localhost')
print(db)
dbse = db.cursor()

dbse.execute("CREATE DATABASE JSONRECORDS1")
cur = db.cursor()

cur.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)
mydb = cx_Oracle.connect('hr/hr@localhost')
cur = mydb.cursor()

cur.execute("CREATE TABLE employee (name varchar(255),age number(2), permanent_staff varchar(255), salary double, dept_and_designation varchar(25))")
cur = mydb.cursor()

cur.execute("SHOW TABLES")

for i in cur:
  print(i)
cur = mydb.cursor()

cur.execute("SHOW COLUMNS FROM employee")

for j in cur:
    print(j)
cur = mydb.cursor()

sql = "INSERT INTO employee (name ,age, permanent_staff,salary,dept_designation) VALUES (%s)"
value = list(for i in res: res[i])

cur.execute(sql, value))





