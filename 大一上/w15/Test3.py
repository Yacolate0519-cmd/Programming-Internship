from tkinter import *
from tkinter import messagebox

def PressButton():
    

if __name__ == '__main__':
    root = Tk()
    btns = []
    for i in range(9):
        for j in range(3):
            btns.append(Button(root , text = ' ' , font = ('Arial' , 20 , 'bold')))
            bnts[-1].config(command = lambda  btn = btns[-1] : PressButton(btn))
            .