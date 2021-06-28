print("BestEnlist Python Bootcamp 2021\nDay16\nBalaji.N.R.")
#Create a lambda function that multiplies argument x with argument y
x=int(input("Enter value for x:"))
y=int(input("Enter Value for y:"))
aj=lambda x,y  : x*y
print(aj(x,y))
print("-"*25)

#Write a Python program to create Fibonacci series to n using Lambda
def fibonacci(count):
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, count)))
    return fib_list[:count]
n=int(input("Enter Number of terms:"))
print(fibonacci(n))
print("-"*25)

#multiply each number of given list with a given number
list1=[]
n=int(input("Enter Number of elements in a list:"))
for i in range(0,n):
    ele=int(input("Enter element:"))
    list1.insert(i,ele)


a=int(input("Enter Number which is to be added to the list:"))
numbers=list(map(lambda number:number*a,list1))
print(numbers)
print("-"*25)

#find numbers divisible by 9 from a list of numbers
my_list=[]
n1=int(input("Enter Number of Elements in a list:"))
for i in range(0,n1):
    ele1=int(input("Enter Element:"))
    my_list.append(ele1)
result=list(filter(lambda x: (x % 9 == 0), my_list))
print("Numbers divisible by 9 are",result)
print("-"*25)

#count the even numbers in a given list of integers
list2=[]
n3=int(input("Enter Number of elements in a list:"))
for i in range(0,n3):
    ele3=int(input("Enter Element:"))
    list2.append(ele3)
even_ele=len(list(filter(lambda x: (x%2 == 0),list2)))
print("Number of even numbers in the list is:")
print(even_ele)
print("-"*25)
