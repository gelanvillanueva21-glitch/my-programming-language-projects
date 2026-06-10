import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Exercise')
window.geometry('400x500')

#Widgets
pad = tk.Text(window)
pad.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'Clcik')
button.pack()

#Binding
pad.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

#Run
window.mainloop()