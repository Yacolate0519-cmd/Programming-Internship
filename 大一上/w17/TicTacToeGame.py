from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Gamer Log In')
root.geometry('500x400+200+100')

root.rowconfigure(0 , weight = 1)
root.rowconfigure(1 , weight = 1)
root.rowconfigure(2 , weight = 1)
root.columnconfigure(0 , weight= 1)
root.columnconfigure(1 , weight= 1)
root.columnconfigure(2 , weight= 1)

player = 0

dic = {'yacolate0519@gmail.com':'950519' , 'Breaddown':'950519' , 'Test':'950519'}

def login(account , password):
    global dic
    if account == '':
        messagebox.showerror('Error' , 'No account exits')
    else:
        if account in dic:
            if password == dic[account]:
                openNewWindow()
            else:
                messagebox.showerror( 'Error' , 'Wrong account or password')
        else:
            messagebox.showerror('Error','Wrong account or password')
        
def signup(account , password):
    global dic
    if account == '':
        messagebox.showerror('Error' , 'Not entered yet')
    else:
        if account in dic:
            messagebox.showerror('Error' , 'Account already exist')
        else:
            dic[account] = password
            messagebox.showerror('Success' , 'Account created successfully')
        

def openNewWindow():
    root.withdraw()
    NewWindow = Toplevel(root)
    NewWindow.title("Tic Tac Toe Game")
    NewWindow.geometry('800x600+100+50')
    
    global player
    player_text = StringVar()
    player_text.set("目前玩家： O")
    def PressButton(btn):
        global player
        if btn['text'] == ' ':
            if player == 0:
                btn['text'] = 'O'
                player = 1
                player_text.set("目前玩家： X")
            else:
                btn['text'] = 'X'
                player = 0
                player_text.set("目前玩家： O")
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
        else:
            count = 0 
            buttons = [bt01 , bt02 , bt03 , bt04 , bt05 ,bt06 ,bt07,bt08,bt09]
            for i in buttons:
                if i['text'] != ' ':
                    count += 1
            if count == 9:
                messagebox.showerror('Error' , 'Draw')
                set_Button_disable()
        
    def set_Button_disable():
        data = [bt01 , bt02 , bt03 , bt04 , bt05 , bt06 , bt07 , bt08 , bt09]
        for i in data:  
            i['state'] = DISABLED
        
    def Restart():
        global player
        player = 0
        player_text.set("目前玩家: O")
        data = [bt01 , bt02 , bt03 , bt04 , bt05 , bt06 , bt07 , bt08 , bt09]
        for i in data:
            i['text'] = ' '
            i['state'] = NORMAL   
        
    
    NewWindow.grid_rowconfigure(0 , weight = 1)
    NewWindow.grid_rowconfigure(1 , weight = 1)
    NewWindow.grid_rowconfigure(2 , weight = 1)
    NewWindow.grid_rowconfigure(3 , weight = 1)
    NewWindow.grid_columnconfigure(0 , weight = 1)
    NewWindow.grid_columnconfigure(1 , weight = 1)
    NewWindow.grid_columnconfigure(2 , weight = 1)


    bt01 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt01))
    bt01.grid(row = 0 , column = 0 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt02 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') ,command = lambda : PressButton(bt02))
    bt02.grid(row = 0 , column = 1 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt03 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') ,command = lambda : PressButton(bt03))
    bt03.grid(row = 0 , column = 2 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt04 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') ,command = lambda : PressButton(bt04))
    bt04.grid(row = 1 , column = 0 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt05 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') ,command = lambda : PressButton(bt05))
    bt05.grid(row = 1 , column = 1 , sticky = NSEW , padx = 10 , pady = 10)

    bt06 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt06))
    bt06.grid(row = 1 , column = 2 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt07 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') ,command = lambda : PressButton(bt07))
    bt07.grid(row = 2 , column = 0 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt08 = Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt08))
    bt08.grid(row = 2 , column = 1 , sticky = NSEW , padx = 10 , pady = 10)
    
    bt09= Button(NewWindow , text = ' ' , font = ('Arial' , 24 , 'bold') , command = lambda : PressButton(bt09))
    bt09.grid(row = 2 , column = 2 , sticky = NSEW , padx = 10 , pady = 10)
    
    btclose = Button(NewWindow , text = 'Close' , font = ("Arial" , 20 , 'bold') , command = lambda : NewWindowClose(NewWindow))
    btclose.grid(row = 3,column = 0)
    
    PlayerLabel = Label(NewWindow , textvariable = player_text , font = ('Arial' , 20 , 'bold'))
    PlayerLabel.grid(row = 3 , column = 1)
    
    btnRestart = Button(NewWindow , text = 'Restart' , font = ("Arial" , 20 , 'bold'), command = Restart)
    btnRestart.grid(row = 3 , column = 2)
    
    def NewWindowClose(self):
        root.deiconify()
        self.destroy()
        
    NewWindow.mainloop()
    
Lab1 = Label(root , text = "帳號" , font = ('Arial' , 25 , 'bold')).grid(row = 0 , column = 0)
account = Entry(root)
account.grid(row = 0 , column = 1 , padx = 2 , pady = 5 , ipadx = 5 , ipady = 5)


Lab3 = Label(root , text = '密碼' , font = ('Arial' , 25 , 'bold')).grid(row = 1 , column = 0)
password = Entry(root)
password.grid(row = 1 , column = 1 , padx = 2 , pady = 5 , ipadx = 5 , ipady = 5)

Login = Button(root , text = 'Log In' , font = ("Arial" , 25 , 'bold') ,width = 10 , relief = 'raised' , command = lambda : login(account.get() , password.get()))
Login.grid(row = 2 , column = 0 , padx = 2 , pady = 5 , ipadx = 5 , ipady = 5)

SignUp = Button(root , text = 'Sign Up' , font = ("Arial" , 25 , 'bold'),relief = 'raised' ,width = 10, command = lambda : signup(account.get() , password.get()))
SignUp.grid(row = 2 , column =  1 , padx = 2 , pady = 5 , ipadx = 5 , ipady = 5)


root.mainloop()