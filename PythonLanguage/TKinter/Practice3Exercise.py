import tkinter as tk
from tkinter import ttk

#Window
Window = tk.Tk()
Window.title('Exercise')
Window.geometry('500x400')

label_Text = ttk.Label(
    Window,
    text = 'Check And Uncheck',
    font = 'Helvetica 20 bold'
    )
label_Text.pack()

#Buttons

def check_uncheck():
    print(button_value.get())
    button_value.set(False)

button_value = tk.BooleanVar()
radio_value = tk.StringVar()

check_radioButton = ttk.Radiobutton(
    Window,
    text = 'Check',
    value = 'A',
    variable = radio_value,
    command = check_uncheck
)

uncheck_radioButton = ttk.Radiobutton(
    Window,
    text = 'Uncheck',
    value = 'B',
    variable = radio_value,
    command = check_uncheck
)

Check_Button = ttk.Checkbutton(
    Window,
    text = 'Check Button',
    variable = button_value,
    command = lambda: print(radio_value.get())
)

Check_Button.pack()
check_radioButton.pack()
uncheck_radioButton.pack()


#Run
Window.mainloop()