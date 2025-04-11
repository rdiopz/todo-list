import json
from tkinter import *
from tkinter import messagebox
import unittest
import os

# Функции для работы с данными
def load_data(filename):
    try:
        with open(filename, "r") as read_file:
            return json.load(read_file)
    except FileNotFoundError:
        return {}

def save_data(filename, data):
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=4)

def add_task(data, task):
    print(data.keys(), type(data.keys()))
    new_id = max(map(int, data.keys()), default=0) + 1
    data[new_id] = task
    return data

def delete_all_data(data):
    return {}

def start(start_dict, task_listbox):
    """Check start file"""
    task_listbox.delete(0, END) # Очистить список перед обновлением
    if start_dict == {}:
        task_listbox.insert(END, "No tasks")
    else:
        for tasks in start_dict:
            task_listbox.insert(END, str(tasks) + ") " + start_dict[tasks])

# Код приложения
def main():
    global start_dict
    window = Tk()
    window.title('ToDo')
    window.geometry('300x230') # window size

    filename = "data_file.json"
    start_dict = load_data(filename)

    task_listbox = Listbox(font = ('Arisal Bold', 10))
    start(start_dict, task_listbox)
    task_listbox.grid(row = 0, column = 0, padx = 15, columnspan = 3, sticky=W+E)

    def add():
        """Add task action"""
        task = task_entry.get()
        if task:
            global start_dict
            start_dict = add_task(start_dict, task)
            start(start_dict, task_listbox)
            task_entry.delete(0, END) 

    def del_data():
        """Delete all data action"""
        global start_dict
        start_dict = delete_all_data(start_dict)
        start(start_dict, task_listbox)
        save_data(filename, start_dict)
        messagebox.showinfo("Ok", "The data was successfully removed")

    def save():
        """Save data action"""
        save_data(filename, start_dict)
        messagebox.showinfo("Ok", "The data was successfully saved")

    task_label = Label(text = "Enter task:", font = ('Arial Bold', 13))
    task_label.grid(row = 1, column = 0) # grid positioning

    task_entry = Entry(window, width = 20, font = ('Arial Bold', 10))
    task_entry.grid(row = 1,column = 1)

    btn_add = Button(text = "Add", command = add, font = ('Arial Bold', 10), width = 5)
    btn_add.grid(row = 1, column = 2)

    btn_del = Button(text = "Delete data", command = del_data, font = ('Arial Bold', 10))
    btn_del.grid(row = 3, column = 0)

    btn_save = Button(text = "Save", command = save, font = ('Arial Bold', 10), width = 5)
    btn_save.grid(row = 3, column = 2)

    window.mainloop() 


if __name__ == '__main__':
    main()
