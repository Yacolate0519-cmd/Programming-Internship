from tkinter import *
from PIL import Image , ImageTk

def clear():
    progress.set('')
    preview.delete(0, 'end') 

def pressButton(button):
    if button == '=':
        try:
            result = eval(preview.get())  
            preview.delete(0, END)
            preview.insert(END, str(result))
        except Exception as e:
            preview.delete(0, END)
            preview.insert(END, 'Error')
    elif button == 'C':
        preview.delete(0, END)
    else:
        preview.insert(END, button)
        
root = Tk()
root.title('計算機')
root.geometry('400x600')
root.config(bg = '#E8C483')

progress = StringVar()
progress.set('')

# Label(root, textvariable=progress).grid(row=0, column=0, columnspan=4)
preview = Entry(root, textvariable=progress, justify=RIGHT, font=('Arial', 20))
preview.grid(row=1, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '.', '+',
    '='
]


row = 3
col = 0
for i, button in enumerate(buttons):
    Button(
        root,
        text=button,
        font=('Arial', 20, 'bold'),
        bg = '#FFFFFF',
        command=lambda b=button: pressButton(b),
    ).grid(row = row , column = col , padx = 10 , pady = 10 , ipadx = 15, ipady = 15 , sticky = 'nsew')
    
    col += 1
    if col > 3:  
        col = 0
        row += 1
        
root.mainloop()