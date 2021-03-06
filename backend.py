import sqlite3

#connect to db
def connect():
    conn = sqlite3.connect("book.db") #connects to db
    cur = conn.cursor() #create cursor object
    #execute sql statement - create tbl if doesn't already exist
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
    #commits changes to db
    conn.commit()
    #close db connection
    conn.close()

def add(title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    #pass NULL - python creates ID automatically
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book") #don't need commit changes when view
    #store data in tuple
    rows = cur.fetchall()
    conn.close()
    return rows

#returns all records from db that match specified criteria
#pass empty strings in case user doesn't fill out all 4 values
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? or year=? or isbn=?",(title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

#deletes book entry from db based on ID
#ID will be first item in tuple when we call this from frontend
def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

#in frontend: user will eventually select entry from listbox then update
#updates book entry to new 4 values based on ID
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book set title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect() #will be executed anytime this script is ran (ie when run frontend)
#TESTING FUNCTIONS
# add("Planets", "Peter Vanguard", 1888, 67858998)
# print(view())
# add("Earth", "John Smith", 1799, 99654895)
# print(view())
# print(search(author="John Smith"))
# delete(2)
# print(view())
update(1,"Space","Mary Matthews", 1919, 46215478)
print(view())
