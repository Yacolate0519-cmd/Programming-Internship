from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Gamer Log In')
root.geometry('500x400+200+100')

root.rowconfigure(0 , weight = 1)
root.rowconfigure(1 , weight = 1)
root.columnconfigure(0 , weight= 1)
root.columnconfigure(1 , weight= 1)

player = 0

def openNewWindow():
    root.withdraw()
    NewWindow = Toplevel(root)
    NewWindow.title("GAME")
    NewWindow.geometry('500x400+100+50')
    
    
    def PressButton(btn):
        global player
        # if btn['text'] == 'Close':
            
        if btn['text'] == ' ':
            if player == 0:
                btn['text'] = 'O'
                player = 1
            else:
                btn['text'] = 'X'
                player = 0
            checkWin()
        else:
            messagebox.showerror("Error" , "This block was already taken")
    def checkWin():
        if bt01['text'] == bt02['text'] == bt03['text'] and bt01['text'] != ' ':
            print(bt01['text'],'win') 
            messagebox.showinfo("Game Over" , bt01['text'] + ' wins')
            set_Button_disable()
        elif bt04['text'] == bt05['text'] == bt06['text'] and bt04['text'] != ' ':
            print(bt03['text'] , 'win')   
            messagebox.showinfo("Game Over" , bt03['text'] + ' wins')
            set_Button_disable()
        elif bt07['text'] == bt08['text'] == bt09['text'] and bt07['text'] != ' ':
            print(bt07['text'] , 'win')  
            messagebox.showinfo("Game Over" , bt07['text'] + ' wins') 
            set_Button_disable()
        elif bt01['text'] == bt04['text'] == bt07['text'] and bt01['text'] != ' ':
            print(bt01['text'] , 'win')   
            messagebox.showinfo("Game Over" , bt01['text'] + ' wins')
            set_Button_disable()
        elif bt02['text'] == bt05['text'] == bt08['text'] and bt02['text'] != ' ':
            print(bt02['text'] , 'win')   
            messagebox.showinfo("Game Over" , bt02['text'] + ' wins')
            set_Button_disable()
        elif bt03['text'] == bt06['text'] == bt09['text'] and bt03['text'] != ' ':
            print(bt03['text'] , 'win')   
            messagebox.showinfo("Game Over" , bt03['text'] + ' wins')
            set_Button_disable()
        elif bt01['text'] == bt05['text'] == bt09['text'] and bt01['text'] != ' ':
            print(bt01['text'] , 'win')   
            messagebox.showinfo("Game Over" , bt01['text'] + ' wins')
            set_Button_disable()
        elif bt03['text'] == bt05['text'] == bt07['text'] and bt03['text'] != ' ':
            print(bt03['text'] , 'win')   
            messagebox.showinfo("Game Over" , bt03['text'] + ' wins')
            set_Button_disable()
        
    def set_Button_disable():
        data = [bt01 , bt02 , bt03 , bt04 , bt05 , bt06 , bt07 , bt08 , bt09]
        for i in data:  
            i['state'] = DISABLED
        
    for i in range(3):
        NewWindow.grid_rowconfigure(i , weight = 1)
        NewWindow.grid_columnconfigure(i , weight = 1)
    
    bt01 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt01))
    bt01.grid(row = 0 , column = 0 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt02 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt02))
    bt02.grid(row = 0 , column = 1 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt03 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt03))
    bt03.grid(row = 0 , column = 2 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt04 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt04))
    bt04.grid(row = 1 , column = 0 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt05 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt05))
    bt05.grid(row = 1 , column = 1 , sticky = NSEW , padx = 10 , pady = 10)

    bt06 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt06))
    bt06.grid(row = 1 , column = 2 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt07 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt07))
    bt07.grid(row = 2 , column = 0 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt08 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt08))
    bt08.grid(row = 2 , column = 1 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt09= Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt09))
    bt09.grid(row = 2 , column = 2 , sticky = NSEW , padx = 10 , pady = 10)
    
    btclose = Button(NewWindow , text = 'Close' , font = ("Arial" , 20 , 'bold') , command = lambda : NewWindowClose(NewWindow))
    btclose.grid()
    
    def NewWindowClose(self):
        root.deiconify()
        self.destroy()
        
    NewWindow.mainloop()
    
Lab1 = Label(root , text = "帳號" , font = ('Arial' , 15 , 'bold')).grid(row = 0 , column = 0)
Lab2 = Entry(root , text = 'Test').grid(row = 0 , column = 1 , padx = 2 , pady = 5)
Lab3 = Label(root , text = '密碼' , font = ('Arial' , 15 , 'bold')).grid(row = 1 , column = 0)
Lab4 = Entry(root , text = 'Test').grid(row = 1 , column = 1 , padx = 2 , pady = 5)
Lab5 = Button(root , text = 'Log In' , command = openNewWindow).grid(row = 2 , column = 0 , padx = 2 , pady = 5)


root.mainloop()