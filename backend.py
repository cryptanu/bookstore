import sqlite3


def connect():
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, year integer, author text, ISBN integer)")
    conn.commit()
    conn.close()


def insert(title,year,author,ISBN):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,year,author,ISBN))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="",year="", author="", ISBN=""):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR year=? OR author=? OR ISBN=?",(title,year,author,ISBN))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()


def update(id, title, year, author, ISBN):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, year=?, author=?, ISBN=? WHERE id=?",(title, year, author, ISBN, id))
    conn.commit()
    conn.close()


connect()
# insert('Purple Hibiscus',1998,'Chimamanda Ngozi',1209390432)
# print(search('Purple Hibiscus'))
# print(view())