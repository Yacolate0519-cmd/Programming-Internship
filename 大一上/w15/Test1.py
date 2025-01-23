from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI_001")
root.geometry("500x400+100+50")

player = 0

def PressButton(btn):
    global player
    if btn['text'] == ' ': 
        if player == 0:
            btn['text'] = 'O'
            player = 1
        else:
            btn['text'] = 'X'
            player = 0
        checkwin()
    else:
        messagebox.showerror("Error", "This cell is already taken!")

     
def checkwin():
    if bt01['text'] == bt02['text'] == bt03['text'] and bt01['text'] != ' ':
        print(bt01['text'],'win') 
        messagebox.showinfo("Game Over" , bt01['text'] + 'wins')
    elif bt04['text'] == bt05['text'] == bt06['text'] and bt04['text'] != ' ':
        print(bt03['text'] , 'win')   
        messagebox.showinfo("Game Over" , bt01['text'] + 'wins')
    elif bt07['text'] == bt08['text'] == bt09['text'] and bt07['text'] != ' ':
        print(bt07['text'] , 'win')  
        messagebox.showinfo("Game Over" , bt01['text'] + 'wins') 
    elif bt01['text'] == bt04['text'] == bt07['text'] and bt01['text'] != ' ':
        print(bt01['text'] , 'win')   
        messagebox.showinfo("Game Over" , bt01['text'] + 'wins')
    elif bt02['text'] == bt05['text'] == bt08['text'] and bt02['text'] != ' ':
        print(bt02['text'] , 'win')   
        messagebox.showinfo("Game Over" , bt01['text'] + 'wins')
    elif bt03['text'] == bt06['text'] == bt09['text'] and bt03['text'] != ' ':
        print(bt03['text'] , 'win')   
        messagebox.showinfo("Game Over" , bt01['text'] + 'wins')
    elif bt01['text'] == bt05['text'] == bt09['text'] and bt01['text'] != ' ':
        print(bt01['text'] , 'win')   
        messagebox.showinfo("Game Over" , bt01['text'] + 'wins')
    elif bt03['text'] == bt05['text'] == bt07['text'] and bt03['text'] != ' ':
        print(bt03['text'] , 'win')   
        messagebox.showinfo("Game Over" , bt01['text'] + 'wins')
    
     
root.grid_rowconfigure(0 , weight = 1)
root.grid_rowconfigure(1 , weight = 1)
root.grid_rowconfigure(2 , weight = 1)
root.grid_columnconfigure(0 , weight = 1)
root.grid_columnconfigure(1 , weight = 1)
root.grid_columnconfigure(2 , weight = 1)




bt01 = Button(root , text = ' ' , command = lambda : PressButton(bt01)).grid(row = 0 , column = 0 , sticky = NSEW , pady = 2 , padx = 2)
bt02 = Button(root , text = ' ' , command = lambda : PressButton(bt02)).grid(row = 0 , column = 1 , sticky = NSEW , pady = 2 , padx = 2)
bt03 = Button(root , text = ' ' , command = lambda : PressButton(bt03)).grid(row = 0 , column = 2 , sticky = NSEW , pady = 2 , padx = 2)
bt04 = Button(root , text = ' ' , command = lambda : PressButton(bt04)).grid(row = 1 , column = 0 , sticky = NSEW , pady = 2 , padx = 2)
bt05 = Button(root , text = ' ' , command = lambda : PressButton(bt05)).grid(row = 1 , column = 1 , sticky = NSEW , pady = 2 , padx = 2)
bt06 = Button(root , text = ' ' , command = lambda : PressButton(bt06)).grid(row = 1 , column = 2 , sticky = NSEW , pady = 2 , padx = 2)
bt07 = Button(root , text = ' ' , command = lambda : PressButton(bt07)).grid(row = 2 , column = 0 , sticky = NSEW , pady = 2 , padx = 2)
bt08 = Button(root , text = ' ' , command = lambda : PressButton(bt08)).grid(row = 2 , column = 1 , sticky = NSEW , pady = 2 , padx = 2)
bt09 = Button(root , text = ' ' , command = lambda : PressButton(bt09)).grid(row = 2 , column = 2 , sticky = NSEW , pady = 2 , padx = 2)


root.mainloop()
