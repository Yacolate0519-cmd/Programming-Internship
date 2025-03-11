from tkinter import *
from PIL import Image , ImageTk

if __name__ == "__main__":
    root = Tk()
    root.title("Image Gallery")
    root.geometry('700x700+100+50')

    style = ('Arial' , 20 , 'bold')
    global images , index , img
    index = 0
    images = ['1.png','2.png','3.png','4.png']
    Images_count = len(images)

    for i in range(5):
        root.grid_rowconfigure(i , weight = 1)
        root.grid_columnconfigure(i , weight = 1)

    for i in range(2 , 5):
        for j in range(5):
            btn = Label(root , text = ' ').grid(row = i , column = j)
    
    img = ImageTk.PhotoImage(file = images[index])
    show = Label(root , image = img , compound = CENTER , bg = '#ccddff')
    show.grid(row = 0 , column = 0 , sticky = NSEW , rowspan = 2 , columnspan = 5)

    def first_image():
        global img , images , index
        index = 0
        img = ImageTk.PhotoImage(file = images[0])
        show.config(image = img)
        
    def left_image():
        global img , images , index
        index -= 1
        if index < 0:
            index = len(images)
        img = ImageTk.PhotoImage(file = images[index])
        show.config(image = img)
    
    def right_image():
        global img , images , index
        index += 1
        
        if index > len(images) - 1:
            index = 0
        
        img = ImageTk.PhotoImage(file = images[index])
        show.config(image = img)
    
    def last_image():
        global img , images , index
        index = len(images)
        img = ImageTk.PhotoImage(file = images[-1])
        show.config(image = img)

    first = Button(root , text = 'First' , font = style , command = first_image).grid(row = 2 , column = 2 , sticky = NSEW)
    left = Button(root , text = '<' , font = style , command = left_image).grid(row = 3 , column = 1 , sticky = NSEW)
    right = Button(root , text = '>' , font = style , command = right_image).grid(row = 3 , column = 3 , sticky = NSEW)
    last = Button(root , text = 'Last' , font = style , command = last_image).grid(row = 4 , column = 2 , sticky = NSEW)
    close = Button(root , text = 'close' , font = style , command = root.destroy).grid(row = 3 , column = 2 , sticky = NSEW)


    root.mainloop()