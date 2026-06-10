import tkinter as tk
from tkinter import ttk

#Functions
def click_func(entry_String):
    print("A Button Was Pressed")
    print(entry_String.get())

def outer_func(parameter):
    def inner_func():
        print("A Button Was Pressed")
        print(parameter.get())
    return inner_func

#Window
window = tk.Tk()
window.title('I Love Chanzine')
window.geometry('400x500')

#Widgets
entry_String = tk.StringVar(value = 'Test')
entry = ttk.Entry(
    window, 
    textvariable = entry_String)
entry.pack()

button = ttk.Button(
    window, 
    text = 'Click', 
    command = outer_func(entry_String)) #Either You Use A Lambda Or Return Type Function
button.pack()

#Run
window.mainloop()