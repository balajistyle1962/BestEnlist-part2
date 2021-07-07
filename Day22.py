# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:40:09 2021

@author: Balaji.N.R.
"""
  
from PIL import Image
import PyPDF2
import requests
from bs4 import BeautifulSoup
import pprint
import cx_Oracle

im1 = Image.open("E:\\BALAJINR\\python\\TajMahal.jpg")
print("Copied Image.....")
print("Showing image.....")
im2 = im1.copy()
im2.show()
 

def PDFmerge(pdfs, output):
    pdfMerger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        pdfMerger.append(pdf)
    with open(output, 'wb') as f:
        pdfMerger.write(f)
        
pdfs = ['E:\\BALAJINR\\python\\OS1.pdf', 'E:\\BALAJINR\\python\\osannexure.pdf']
output = 'combined_pdf.pdf'
print("Reading the PDF.....")
PDFmerge(pdfs=pdfs, output=output)
print("PDF merged succesfully")




res = requests.get('https://news.ycombinator.com/news?p=2')

soup =  BeautifulSoup(res.text, 'lxml')

titleRows=soup.find_all('tr','athing')

votesRows=soup.find_all('span','score')

titles=[]
votes=[]

for i in titleRows:
    title=i.find('a','storylink').text
    titles.append(title)

for i in votesRows:
    vote=i.text.split()[0]
    votes.append(vote)

print("Website Scrapped and the Values are stores in python objects")


DBDataRows=list(map(list,zip(titles,votes)))

try:
    con = cx_Oracle.connect("hr/hr@localhost")
    cur=con.cursor()
    print("Connected to DataBase")

    cur.execute("create table WeBScrapDB(title varchar(100),votes number(10))")
    print("Table Created")
    cur.executemany("insert into WeBScrapDB values(:1,:2)",DBDataRows)
    con.commit()

    print("Printing the titles having more than 500 votes ")

    cur.execute("select * from WeBScrapDB where votes>500")

    DBRows=cur.fetchall()

    for i in DBRows:
        print("Title : ",i[0])
        print("Votes : ",i[1])

    
    print("Values Inserted")

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
con.close()