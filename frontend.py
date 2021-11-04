"""
This program stores book info including:
Title, Year, Author, and ISBN.

User can:
View all records
Search for an entry
Add Entry
Update Entry
Delete Entry
close
"""

import tkinter
from tkinter import *
import backend

#in backend we have list of tuples
#view function inserts each tuple as new row inside Listbox
def view_command():
    list.delete(0,END)
    #backend.view is list of tuples in backend - is list obj
    for row in backend.view():
        #insert into listbox - new rows put at end of listbox
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    #get param from entry widgets
    #change param to plain str obj
    for row in backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        list.insert(END,row)

window=Tk()
window.title("Bookstore Inventory")

#labels
b1=Label(window, text="Title")
b1.grid(row=0,column=0)
b2=Label(window, text="Year")
b2.grid(row=1,column=0)
b3=Label(window, text="Author")
b3.grid(row=0,column=2)
b4=Label(window, text="ISBN")
b4.grid(row=1,column=2)

#entries
title_value=StringVar()
e1=Entry(window, textvariable=title_value, width=14)
e1.grid(row=0,column=1)

year_value=StringVar()
e2=Entry(window, textvariable=year_value,width=14)
e2.grid(row=1,column=1)

author_value=StringVar()
e3=Entry(window, textvariable=author_value,width=14)
e3.grid(row=0,column=3)

isbn_value=StringVar()
e4=Entry(window, textvariable=isbn_value,width=14)
e4.grid(row=1,column=3)

#buttons
b1=Button(window, text="View all", width=14, command=view_command)
b1.grid(row=2,column=3)
b2=Button(window, text= "Search entry",width=14, command=search_command)
b2.grid(row=3,column=3)
b3=Button(window, text="Add entry",width=14)
b3.grid(row=4,column=3)
b4=Button(window, text="Update",width=14)
b4.grid(row=5,column=3)
b5=Button(window, text="Delete",width=14)
b5.grid(row=6,column=3)
b6=Button(window, text="Close",width=14)
b6.grid(row=7,column=3)

#listbox
list=Listbox(window,height=6,width=35)
list.grid(row=2,column=0, rowspan=6, columnspan=2)

#scrollbar for listbox
s=Scrollbar(window)
s.grid(row=2,column=2, rowspan=6)
#apply config method to listbox and scrollbar obj
list.configure(yscrollcommand=s.set)
s.configure(command=list.yview) #when scroll the vertial view chages

window.mainloop()
