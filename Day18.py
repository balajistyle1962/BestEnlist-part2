# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:42:43 2021

@author: USER
"""

import cx_Oracle
print("BestEnlist Bootcamp 2021\nDay18\nBalaji.N.R.")
#Create a DB with doctor and doctor ID & patients visited
con=cx_Oracle.connect('hr/hr@localhost')
cur=con.cursor()
cur.execute("Create table Doctor(doctor_id int,doctor_name varchar(20),patient_visited int)")
try:
    cur.execute("insert into Doctor values(1,'tara',3)")
    cur.execute("insert into Doctor values(2,'tharani',8)")
    cur.execute("insert into Doctor values(4,'mukesh',7)")
    cur.execute("insert into Doctor values(10,'sanjay',0)")
    con.commit()
    print("Values inserted Sucessfully")
    print("*"*25)
except Exception as err:
    print("Failed to insert values",err)

#Get the doctor(s) who have more than 5 patients visited
cur.execute("select * from doctor where patient_visited>5")
result=cur.fetchall()
j=0
for i in result:
    print("Row",(j+1),":",i)
    j+=1
    con.commit()
print("*"*25)

#Get the doctors with no patients visit
cur.execute("select * from doctor where patient_visited=0")
re=cur.fetchall()
j=0
for i in re:
    print("Row",(j+1),":",i)
    j+=1
    con.commit()
print("*"*25)
    
con.close()