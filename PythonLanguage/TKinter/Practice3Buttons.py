import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Buttons')
window.geometry('500x400')

#Button

def click():
    print('Hello World')
    if radio_String.get() == '1':
        print("You Click The RadioButton 1")
    else:
        print("You Click The RadioButton 2")


button_String = tk.StringVar(value = "Click")
check_String1 = tk.StringVar()
check_String2 = tk.StringVar()
radio_String = tk.StringVar()

click_button = ttk.Button(
    window, 
    command = click, 
    textvariable = button_String)
click_button.pack(pady = 10)

check_button1 = ttk.Checkbutton(
    window, 
    text = 'CheckBox 1', 
    command = lambda: print(check_String1.get()), 
    variable = check_String1, 
    onvalue = 'Hello', 
    offvalue = 'World')
check_button1.pack(pady = 10)
check_button2 = ttk.Checkbutton(
    window,
    text = 'CheckBox 2',
    command = lambda: check_String1.set('World'),
    #variable = check_String2,
    #onvalue = 'Six',
    #offvalue = 'Seven'
)
check_button2.pack(pady = 10)

radio_button1 = ttk.Radiobutton(
    window, 
    text = "RadioButton1", 
    value = 1,
    variable = radio_String,
    command = lambda: print(radio_String.get()))
radio_button1.pack()
radio_button2 = ttk.Radiobutton(
    window, 
    text = 'RadioButton2', 
    value = 0, 
    variable = radio_String,
    command = lambda: print(radio_String.get()))
radio_button2.pack()

#Run
window.mainloop()