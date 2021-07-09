# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:51:31 2021

@author: Balaji.N.R.

"""
print("BestEnlist Python Bootcamp\nBalaji.N.R.\nDay25\n")
import datetime
#convert a string to datetime 
str1=input("Enter String(format:Mon Date Year time(Am/Pm))")
date1=datetime.datetime.strptime(str1,'%b %d %Y %I:%M%p')
print(date1)

#subtract five days (last working day) from current date
print("Printing five day before today:")
date2 = datetime.datetime.now()
days = datetime.timedelta(5)
new_date = date2 - days
print(new_date)

#convert the date to datetime using a function 
def sample(date3):
    print(datetime.datetime.combine(date3, datetime.datetime.min.time()))
print("Converting date to datetime")
date3 = datetime.date.today()
sample(date3)


#print next 7 days (week) starting from today
print("Printing next week starting from today:")
date4=datetime.date.today()
for i in range(0,7):
    print(date4+datetime.timedelta(i))
    
