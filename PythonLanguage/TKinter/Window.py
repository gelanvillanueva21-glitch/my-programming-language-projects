import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    
    if mile_input == 67:
        output_string.set('Hello World')
    else:
        km_output = mile_input * 1.61
        output_string.set(km_output)

#_______Window_______
window = ttk.Window(themename = 'darkly')
window.title('Demo Window')
window.geometry('300x300')

#_______Title_______
title = ttk.Label(master = window,
                    text = 'Miles to Kilometers',
                    font = 'Helvetica 20 bold')
title.pack()

#_______Input_______
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, 
                  textvariable = entry_int)
convert_button = ttk.Button(master = input_frame, 
                            text = 'Convert', 
                            command = convert)
entry.pack(side = 'right', padx = 5)
convert_button.pack(side = 'left')
input_frame.pack(pady = 5)

#_______Output_______
output_string = tk.StringVar()
output = ttk.Label(master = window, 
                   text = 'Output', 
                   font = 'Calibre 20', 
                   textvariable = output_string)
output.pack(pady = 5)

#_______Run_______
window.mainloop()
