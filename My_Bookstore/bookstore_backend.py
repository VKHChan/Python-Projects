# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:27:40 2018

@author: V Chan
"""

import sqlite3

# function to connect to the database
def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # create table if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

# function to insert new record
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # insert record
    cur.execute("INSERT OR IGNORE INTO book VALUES ((select ID from book where title=?), ?,?,?,?)", (title, title, author, year, isbn))
    conn.commit()
    conn.close()

# function to view the records
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # select all data
    cur.execute("SELECT * from book")
    rows = cur.fetchall()
    conn.close()
    
    return rows

# function to search the database
# user can search by either title, author
# year or ISBN
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # select all data
    cur.execute("SELECT * from book WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows
    
# function to delete an entry
# the user selects the entry from the screen
# and press the delete button to delete
def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # insert record
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

# function to update an entry
# the user selects the entry from the screen
# enter information to update and then
# press update button to update
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    # insert record
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

# always estabish connection when 
# the app is opened.
connect()
