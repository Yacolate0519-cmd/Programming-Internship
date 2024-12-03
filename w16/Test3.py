from tkinter import *
from tkinter import ttk

def calculate():
    v1 = float(in1.get())
    v2 = float(in2.get())
    if combo1.current() == 0:
        lab1['text'] = str((v1 - 80) * 0.7)
    elif combo1.current() == 1:
        lab1['text'] = str((v1 - 70) * 0.6)
        
root = Tk()
root.title('Entry-Demo')
root.geometry('500x100+200+100')
root.rowconfigure(0,weight = 1)
root.rowconfigure(1,weight = 1)
root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.columnconfigure(2,weight = 1)
root.columnconfigure(3,weight = 1)
root.columnconfigure(4,weight = 1)

in1 = Entry(root , width = 10)
in1.grid(row = 1 , column = 0 , pady = 5 , padx = 2)
combo1 = ttk.Combobox(root , values = ['男','女'],width = 3)
combo1.current(0)
combo1.grid(row = 1 , column = 1 , pady = 5 , padx = 2)

in2 = Entry(root , width = 10)
in2.grid(row = 1 , column = 2, pady = 5 , padx = 2)

eqBtn = Button(root , text = '=',
               command = calculate)
eqBtn.grid(row = 1 , column = 3)


label1 = Label(root , text = '身高')
label1.grid(row = 0 , column = 0 , pady = 5 , padx = 2)

label1 = Label(root , text = '性別')
label1.grid(row = 0 , column = 1 , pady = 5 , padx = 2)

label1 = Label(root , text = '體重')
label1.grid(row = 0 , column = 2 , pady = 5 , padx = 2)

label1 = Label(root , text = 'BMI')
label1.grid(row = 0 , column = 4 , pady = 5 , padx = 2)

lab1 = Label(root , text = '0')
lab1.grid(row = 1 , column = 4 , padx = 2 , pady = 5)

root.mainloop()
