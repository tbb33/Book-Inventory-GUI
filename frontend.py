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
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)
e2=Entry(window, textvariable=e2_value)
e2.grid(row=1,column=1)
e3=Entry(window, textvariable=e3_value)
e3.grid(row=0,column=3)
e4=Entry(window, textvariable=e4_value)
e4.grid(row=1,column=3)



window.mainloop()
