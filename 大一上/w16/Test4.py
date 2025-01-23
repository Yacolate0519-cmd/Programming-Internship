from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Entry-Demo')
root.geometry('600x500+200+100')

def openNewWindow():
    root.withdraw()
    newWindow = Toplevel(root)
    newWindow.title('New Window')
    newWindow.geometry('400x300')
    Label(newWindow , text = 'This is a new Window').grid()
    
    btn = Button(newWindow,
                 text = 'Close',
                 command = lambda : newWindowClose(newWindow)).grid(pady = 5)

def newWindowClose(self):
    root.deiconify()
    self.destroy()

lab1 = Label(root , text = 'This is the main window')
lab1.grid(pady = 10)
btn1 = Button(root,
              text = 'Click to open a new window',
              command = openNewWindow)
btn1.grid(pady = 10)

root.mainloop()
