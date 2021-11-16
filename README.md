The app uses Tkinter (a GUI library) and sqlite3 (a library that interacts with sqlite database).

This program stores book info in SQLite database:
Title, Year, Author, and ISBN.

User can:
View all records,
Search for an entry,
Add Entry,
Update Entry,
Delete Entry,
Close the window




Two files are needed for this project:
1. frontend.py - constructs GUI, run this file to run the entire program, connects frontend functions to backend.py
2. backend.py - creates and connects to database "book.db", creates table and changes the database through various functions

Optional file - book.db is a sample file of what the database file may look like. User can use this file to begin by putting all 3 files in the same folder.
