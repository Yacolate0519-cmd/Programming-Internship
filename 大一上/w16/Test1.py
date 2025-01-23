from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title('計算機')
root.geometry('400x600')

password = input('Enter the password: ')

def btn_click(btn):
    global password
    if btn == 'OK':
        try:
            if password == lab.get():
                lab.delete(0,END)
                lab.insert(END , "密碼正確")
                messagebox.showinfo(message = "密碼正確")
            else:
                lab.delete(0,END)
                lab.insert(END , '密碼錯誤')
                messagebox.showinfo(message = "密碼錯誤")
        except Exception:
            lab.delete(0,END)
            lab.insert(END, 'ERROR')
    elif btn == 'C':
        lab.delete(0,END)
    else:
        lab.insert(END,btn)
    

for i in range(13):
    root.grid_rowconfigure(i , weight = 1)
    root.grid_columnconfigure(i , weight = 1)

already = []
# Preview_label = Entry(root , text = '' , font = ("Arial" , 20 , 'bold')).grid(row = 0 , column = 0 , padx = 2 , pady = 2)

lab = Entry(root , font = ('Arial' , 20 , 'bold') , justify = RIGHT , bd = 2 , relief = 'solid')
lab.grid(row = 0 , column = 0 , columnspan = 4 , padx = 10 , pady = 10 , sticky = NSEW)


for _ in range(300):        
    i = random.randint(1,3)
    j = random.randint(0,2)
    if [i,j] not in already:
        already.append([i,j])
        
# print(already)

# 10 11 12
# 20 21 22
# 30 31 32
        
for i in range(9): 
    btn = Button(root , text = i , font = ('Arial' , 20 , 'bold') , command = lambda t = i : btn_click(t))
    btn.grid(row = already[i][0] , column = already[i][1] , ipadx = 20 , ipady = 20 ,  padx = 2 , pady = 2)       
        
btn = Button(root , text = 'C' , command = lambda : btn_click('C') , font = ("Arial" , 20 , 'bold')).grid(row = 4 , column = 0 , padx = 2 , pady = 2 , ipadx = 15 , ipady = 15)
btn = Button(root , text = 'OK' , command = lambda : btn_click("OK") , font = ("Arial" , 20 , 'bold')).grid(row = 4 , column = 2 , padx = 2 , pady = 2 , ipadx = 10 , ipady = 10)


root.mainloop()
