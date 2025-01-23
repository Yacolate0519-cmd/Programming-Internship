from tkinter import *

def click(button):
    if button == "=":
        try:
            result = eval(lab.get())  
            lab.delete(0, END)
            lab.insert(END, str(result))
        except Exception:
            lab.delete(0, END)
            lab.insert(END, "Error")
    elif button == "C":
        lab.delete(0, END)  
    else:
        lab.insert(END, button)  

window = Tk()
window.title("計算器")
window.geometry("400x400")

lab = Entry(window, font=("Arial", 24), justify="right", bd=2, relief="solid")
lab.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

for i, text in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    Button(window, text=text, font=("Arial", 18), 
           bg="#ffffff", fg="#000000",
            command=lambda t=text: click(t)).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")
    
window.mainloop()