from tkinter import *

op = 0
val1 = 0
opCount = 0

def btn_click(btn):
    global op , val1
    if btn['text'] in ['+' , '-' , '*' , '/']:
        val1 = float(label['text'])
        if btn['text'] == '+' :
            op = 1
        elif btn['text'] == '-':
            op = 2
        elif btn['text'] == '*':
            op = 3
        elif btn['text'] == '/':
            op = 4
        op = 0
    elif btn['text'] == '=':
        if op == 1:
            val1 += float(label['text'])
            label.config(text = str(val1))
        elif op == 2:
            val1 -= float(label['text'])
            label.config(text = str(val1))
        elif op == 3:
            val1 *= float(label['text'])
            label.config(text = str(val1))
        elif op == 4:
            val1 /= float(label['text'])
            label.config(text = str(val1))       
    else:
        if op != 0:
            if opCount ==1:
                label.config(text = btn['text'])
                opCount = 0
            else:
                label.config(text = label['text'] + btn['text'])
        else:
            label['text'] == '0':
                
                

if __name__ == '__main__':
    root = Tk()
    root.geometry('500x500')

    
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    
    label = Label(
        root, text='0', font=('Arial', 20, 'bold'), justify=RIGHT,
        anchor=E, bg='#ccddee'
    )
    label.grid(row=0, column=0, columnspan=4, sticky=NSEW)

   
    btn_labs = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    
    for i in range(4):
        for j in range(4):
            btn = Button(
                root, text=btn_labs[i*4 + j], font=('Arial', 20, 'bold'))
            btn[-1].config(command=lambda btn=btn_labs[i * 4 + j]: btn_click(btn))
            btn.grid(row=i + 1, column=j, sticky=NSEW)

    
    root.resizable(0, 0)
    root.mainloop()