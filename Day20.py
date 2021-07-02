# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 19:18:28 2021

@author: Balaji.N.R.

"""

import cx_Oracle
print("BestEnlist Bootcamp python 2021\nDay20\nBalaji.N.R.")
con=cx_Oracle.connect("hr/hr@localhost")
cur=con.cursor()
#cur.execute("create table Employee(emp_id int,emp_name varchar(20),salary float,company varchar(20))")
cur.execute("insert  into Employee values(1001,'balaji',50000,null) ")
cur.execute("insert  into Employee values(1002,'sudarsan',70000,'zoho')")
cur.execute("insert into Employee values(1003,'rubesh',75000,'amazon')")
cur.execute("insert  into Employee values(1004,'karthik',80000.50,'tcs')")
cur.execute("select * from Employee")



#get the maximum and minimum salary from employees table
cur.execute("select  max(salary) from Employee")
result=cur.fetchall()
for i in result:
    print("Maximum of salary",i)


cur.execute("select min(salary) from Employee")
result1=cur.fetchall()
print("Minimum Salary:",result1)


#get the number of employees working with the company
cur.execute("select company from Employee ")
result2=cur.fetchall()
print("Companys:")
for j in result2:
    print(j)
print("Number of employees working with company",len(result2))


#get the first 3 characters of first name from employees table
cur.execute("select substr(emp_name,1,3) from Employee")
result3=cur.fetchall()
for k in result3:
    print(k)
con.commit()