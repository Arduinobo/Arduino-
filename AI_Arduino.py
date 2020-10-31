import tkinter
from tkinter import *
from tkinter import messagebox
from subprocess import *
import os
from playsound import playsound
import datetime

w = 1

if w <= 5:
    print('''
-------------------------------------------------------------------------------------------------------------------
                                            |AI Arduino|
-------------------------------------------------------------------------------------------------------------------                                            
''')

print("Date - ")
now=datetime.datetime.now()
print(now.strftime("%y-%m-%d")) 

root = tkinter.Tk()
root.geometry("250x250")

photo = PhotoImage(file="icons8-microphone-50.png")
def btnclick():
    Popen('python testing.py') 
btn = Button(
    root,
    image=photo,
    command=btnclick,
    border=0,
)
btn.pack(pady=50)

root.mainloop()