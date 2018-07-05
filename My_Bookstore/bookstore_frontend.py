# -*- coding: utf-8 -*-
"""
The graphic user interface for the bookstore app.

The bookstore app stores the following information of a book:
    Title, Author, Year, ISBN
The user can:
    view all records
    search an entry
    add entry
    update an entry
    delete an entry
    close

Created on Wed Jul  4 19:12:55 2018

@author: V Chan
"""
from tkinter import *
import bookstore_backend

# function that display the record
# in the list panel
def view_command():
    list1.delete(0, END)
    for row in bookstore_backend.view():
        list1.insert(END, row)

# function that calls the search
# function from the backend
def search_command():
    list1.delete(0, END)
    for row in bookstore_backend.search(title_text.get(),
                                        author_text.get(),
                                        year_text.get(),
                                        isbn_text.get()):
        list1.insert(END,row)

def insert_command():
    bookstore_backend.insert(title_text.get(),
                             author_text.get(),
                             year_text.get(),
                             isbn_text.get())
    list1.delete(0,END)
    view_command()

def get_select_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        
        # fill the entry values with the values
        # of the selected book record
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def update_command():
    bookstore_backend.update(selected_tuple[0], 
                             title_text.get(),
                             author_text.get(),
                             year_text.get(),
                             isbn_text.get())
    list1.delete(0,END)
    view_command()

def delete_command():
    bookstore_backend.delete(selected_tuple[0])
    list1.delete(0,END)
    view_command()


window = Tk()

window.wm_title("My Bookstore")
# add the labels
# there are four labels in total:
# Title, Author, Year and ISBN
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# add the entry 
# there are four entries in total
# one per label
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)
isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# add the listbox that display the books
# in the current database
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# add the scroll bar that allows
# user to scroll down to see all records
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2)
# link the scrollbar to the listbox
# specify it's for vertical view (y)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_select_row)

# add the buttons, there are 6 buttons:
# View all, Search entry, Add entry,
# Update, Delete and Close
b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = Button(window, text="Add entry", width=12, command=insert_command)
b3.grid(row=4, column=3)
b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()




