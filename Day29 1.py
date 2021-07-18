# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 11:00:22 2021

@author: Balaji.N.R.

"""
import random
count_user=0
count_com=0
user_name=input("Enter User Name:")
while True:
    print("Stone or Paper or Scisssor")
    user=input("Enter Your input:")
    possible=["Stone","Paper","Scissor"]
    com=random.choice(possible)
    if(user==com):
        print("Match Tied!")
    if(user=="Stone"):
        if(com=="Paper"):
            print("Computer Wins!")
            count_com+=1
        else:
            print(user_name,end=" ")
            print("wins!")
            count_user+=1
    elif(user=="Paper"):
        if(com=="Stone"):
            print(user_name,end=" ")
            print("wins!")
            count_user+=1
        else:
            print("Computer Wins!")
            count_com+=1
    elif(user=="Scissor"):
        if(com=="Paper"):
            print(user_name,end=" ")
            print("wins!")
            count_user+=1
        else:
            print("Computer Wins!")
            count_com+=1
    print("************Points********")
    print("Computer :",count_com)
    print(user_name,end=" ")
    print(":",count_user)
    ch=input("Do You Want to Continue(Y/N)")
    if(ch=='N'):
        print("Final Scores:")
        if(count_com>count_user):
            print("Final Winner Computer")
            print("You Lose!!!")
        else:
            print("Final Winner",user_name)
            print("Congratulations!!!")
        break
    else:
        continue
    
            
            
    