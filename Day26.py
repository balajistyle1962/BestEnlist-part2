# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Enumerate a python list and try to print the counter with the list value
print("BestEnlist Python Bootcamp\nDay26\nBalaji.N.R.")
n=int(input("Enter Number of elements in the list:"))
list1=[]
for i in range(0,n):
    a=input("Enter %d element"%(i))
    list1+=a
print(list1)
    
list2=enumerate(list1,0)
print(list(list2))

list3=[]
for j in range(0,n):
    b=input("Enter %d element"%(j))
    list3+=b


tuple1=tuple(list3)
print(tuple1)
tuple2=enumerate(tuple1,0)
print(tuple(tuple2))
