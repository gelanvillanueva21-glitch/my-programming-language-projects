import tkinter as tk
from tkinter import ttk

#Window

window = tk.Tk()
window.title('Exercise')
window.geometry('300x300')

def click_Button():
    print(string_variable.get())
    string_variable.set('Pressed Button')

#Variable

string_variable = tk.StringVar()

#Widget

first_entry = ttk.Entry(master = window, 
                        textvariable = string_variable)
first_entry.pack(pady = 15)

middle_label = ttk.Label(master = window, 
                         textvariable = string_variable, 
                         font = 'Helvetica 20 bold')
middle_label.pack(pady = 15)

second_entry = ttk.Entry(master = window, 
                         textvariable = string_variable)
second_entry.pack(pady = 15)

click_button = ttk.Button(master = window, 
                          text = 'Click', 
                          command = click_Button)
click_button.pack(pady = 15)

#Run

window.mainloop()
