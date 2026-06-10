import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Getting and Setting widgets')
window.geometry('500x500')

def button_func():
    print(entry.get())
    entry_text = ''

    if entry.get() == '67':
        entry_text = 'SIXSEVEN'
    else:
        entry_text = entry.get()
    #label.configure(text = 'You Click The Button')
    label['text'] = entry_text
    entry['state'] = 'disabled'

def enable_func():
    label['text'] = 'TEXT'
    entry['state'] = 'enabled'
#Widgets

label = ttk.Label(master = window, text = 'TEXT')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

first_button = ttk.Button(master = window, text = 'Click', command = button_func)
first_button.pack()

second_button = ttk.Button(master = window, text = 'Enabled', command = enable_func)
second_button.pack()

#Run
window.mainloop()