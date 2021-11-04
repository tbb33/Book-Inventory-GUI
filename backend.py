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


connect() #will be executed anytime this script is ran (ie when run frontend)
#TESTING FUNCTIONS
# add("Planets", "Peter Vanguard", 1888, 67858998)
# print(view())
add("Earth", "John Smith", 1799, 99654895)
print(view())
print(search(author="John Smith"))
