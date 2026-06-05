import tkinter as tk
from tkinter import ttk

def button_Func():
    pass


def print_Hello():
    print('Hello')

#_____WINDOW______
window = tk.Tk()
window.title('Widget')
window.geometry('800x500')

#_____WIDGETS_____
text = tk.Text(master = window)
text.pack()

#_____ENTRY_____
entry = ttk.Entry(master = window)
entry.pack()

hello = ttk.Button(
    master = window, 
    text = 'Print', 
    command = lambda: 
        print('Hello'))
hello.pack()

#_____BUTTON_____
button = ttk.Button(
    master = window, 
    text = 'Click', 
    command = button_Func)
button.pack()

#_____RUN_____
window.mainloop()