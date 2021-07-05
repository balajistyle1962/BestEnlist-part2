# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:24:24 2021

@author: Balaji.N.R.

"""

print("BestEnlist Bootcamp Python 2021\nDay 21\nBalaji.N.R.")
#use zip() and list()function.
a=("faf","abd","amla")
b=("Ms","virat","bhuvi")
x=zip(a,b)
print(list(x))
print("-"*30)

#range from 1 to 8
list1=list(range(1,9))
print(list1)
#zip, merge the given list and the range together to create a new list of tuples.
print("Enter Eight values in form of list in single line")
list2=list(map(int,input().split()))
list3=zip(list1,list2)
print(list(list3))
print("-"*30)

#Using sorted() function, sort the list in ascending order.
tuple1=tuple()
ls=list(tuple1)
print("Enter Number of Elements in the tuple")
n=int(input())
for i in range(0,n):
    ele=int(input("Enter Elements:"))
    ls.append(ele)
tuple2=tuple(ls)

print("Sorted Elements in the list is:")
sort=sorted(tuple2)
print(sort)
print("-"*30)
#filter the even numbers so that only odd numbers are passed to the new list
def even(n):
    if(n%2!=0):
        return True
    else:
        return False

print("List of numbers in a single line")
n=list(map(int,input().split()))
print("Printing only odd numbers:")
filtered = filter(even,n)
for i in filtered:
    print(list(filtered))
print("-"*30)


