# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 05:06:39 2021

@author: Balaji.N.R.
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='gold', relief='groove')
canvas1.pack()

label1 = tk.Label(root, text="Image Converter", bg='red')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browse_png = tk.Button(text="Select JPG file", command=getPNG, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browse_png)

def convert():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)

saveasbutton = tk.Button(text="Convert JPG to PNG", command=convert, bg='violet', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveasbutton)
root.mainloop()