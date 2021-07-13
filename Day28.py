# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 21:16:42 2021

@author: Balaji.N.R.
"""
print("BestEnlist Bootcamp Python\nBalaji.N.R.\nDay28")
import threading
import datetime
#Define a subclass using threading.Thread class.
class myThread (threading.Thread):
    #Instantiate the subclass and trigger the thread.
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("\nStarting " + self.name)
        print_date(self.name, self.counter)
        print("Exiting " + self.name)
        
def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print("{}[{}]: {}".format( threadName, counter, datefields[0] ))

thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 3)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("\nExiting the Program!!!")