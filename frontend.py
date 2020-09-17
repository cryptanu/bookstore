"""
A program that stores book data:
Title, Author
Year, ISBN

Users can:
View all records
Search for an entry
Add an entry
Update a previous entry
Delete entry(ies)
Close the app
"""

from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    try:
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
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


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END,row)


def search_command():
    list1.delete(0, END)
    for entry in backend.search(title_text.get(), year_text.get(), author_text.get(), ISBN_text.get()):
        list1.insert(END, entry)


def insert_command():
    backend.insert(title_text.get(), year_text.get(), author_text.get(), ISBN_text.get())
    list1.delete(0, END)
    list1.insert(END,(title_text.get(), year_text.get(), author_text.get(), ISBN_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def update_command():
    backend.update(selected_tuple[0],title_text.get(), year_text.get(), author_text.get(), ISBN_text.get())
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def close_command():
    window.destroy()


window = Tk()

window.wm_title('Bookstore')
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Year")
l2.grid(row=0, column=2)

l3 = Label(window, text="Author")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

year_text = StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(row=0, column=3)

author_text = StringVar()
e3 = Entry(window, textvariable=author_text)
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=8, width=50)
list1.grid(row=2,column=0, rowspan=8, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=8)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)
b1 = Button(window, text='View All', width = 15, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width = 15, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width = 15, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width = 15, command = update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width = 15, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width = 15, command=close_command)
b6.grid(row=7, column=3)

window.mainloop()