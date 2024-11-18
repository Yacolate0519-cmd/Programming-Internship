#Button

from tkinter import *

x = 0

def count(lab):
    global x
    x += 1
    lab.config(text=str(x))

def decount(lab):
    global x
    x -= 1
    lab.config(text = str(x))
    
    
def reset(lab):
    global x
    x = 0
    lab.config(text = str(x))
    

    
if __name__ == '__main__':
    root = Tk()
    root.title("GUI_001")
    root.geometry("500x400+100+50")
    
    label = Label(root , width = 15 , height = 3 , text = str(x) ,font = 'Arial 20 bold', justify = CENTER , bg = '#ccddef' )
    label.pack()
    
    btnPush = Button(root , width = 15 , height = 2 , text = 'Push' , foreground = "#ff2233" , font = 'Arial 20 bold' , command = lambda:count(label))
    btnPush.pack(pady=10)
    
    btnPush1 = Button(root , width = 15 , height = 2 , text = 'Pull' , foreground = "#ff2233" , font = 'Arial 20 bold' , command = lambda:decount(label))
    btnPush1.pack(pady = 10)
    
    
    btnPush2 = Button(root , width = 15 , height = 2 , text = 'reset' , foreground = "#ff2233" , font = 'Arial 20 bold' , command = lambda:reset(label))
    btnPush2.pack(pady = 10)
    
    
    root.mainloop()
    
