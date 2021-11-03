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
e1_value=StringVar()
e2_value=StringVar()
e3_value=StringVar()
e4_value=StringVar()
e1=Entry(window, textvariable=e1_value, width=14)
e1.grid(row=0,column=1)
e2=Entry(window, textvariable=e2_value,width=14)
e2.grid(row=1,column=1)
e3=Entry(window, textvariable=e3_value,width=14)
e3.grid(row=0,column=3)
e4=Entry(window, textvariable=e4_value,width=14)
e4.grid(row=1,column=3)

#buttons
b1=Button(window, text="View all", width=14)
b1.grid(row=2,column=3)
b2=Button(window, text= "Search entry",width=14)
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
list=Listbox(window)
list.grid(row=2,column=0, rowspan=6, columnspan=2)

#scrollbar for listbox
s=Scrollbar(window)
s.grid(row=2,column=2, rowspan=6)
#apply config method to listbox and scrollbar obj
list.configure(yscrollcommand=s.set)
s.configure(command=list.yview) #when scroll the vertial view chages

window.mainloop()
