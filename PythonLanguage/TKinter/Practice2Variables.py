import tkinter as tk
from tkinter import ttk

#Window

window = tk.Tk()
window.title('Variables')
window.geometry('400x400')

#Functions

def click_button():
    print(string_var.get())
    string_var.set('Button Pressed')

#Variables

string_var = tk.StringVar(value = 'Enter Text')

#Widgets

label = ttk.Label(master = window, textvariable = string_var)
label.pack()
entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()
button = ttk.Button(master = window, text = 'click', command = click_button)
button.pack()

#Run
window.mainloop()
