import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Event Binding')
window.geometry('400x500')

def location(event):
    print(f'x: {event.x} y: {event.y}')

#Widgets
pad = tk.Text(window)
pad.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'Clcik')
button.pack()

#Event Binding
#button.bind('<Alt-KeyPress-a>', lambda event: print('Hello World'))
#window.bind('<Motion>', location)

#window.bind('<KeyPress>', lambda event: print(f'A Button Key Was Pressed ({event.char})'))
entry.bind('<FocusIn>', lambda event: print('Entry field was Selected'))
entry.bind('<FocusOut>', lambda event: print('Entry field was Unselected'))


#Run
window.mainloop()