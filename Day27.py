# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:36:11 2021

@author: USER
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
 
print("BestEnlist Python Bootcamp 2021\nDay27\nBalaji.N.R.")
result = requests.get('https://www.worldometers.info/food-agriculture/india-food-agriculture/')
sample=BeautifulSoup(result.text,'lxml')
count=sample.find_all('div' ,class_= 'panel-body')
data = []
for i in count:
    span = i.find('span')
    data.append(span.string)
print(data)

#copying content to Excel.
df = pd.DataFrame({"Indian food and agriculture": data})
df.index = ['People in india','People in the world','Forest area in India','Cropland in India','Pesticide use in India','Pesticides per hectare']
df.to_csv('Green India.csv')