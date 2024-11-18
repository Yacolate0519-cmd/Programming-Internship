from tkinter import *
from PIL import Image , ImageTk    
    
if __name__ == '__main__':
    root = Tk()
    root.title("GUI_001")
    root.geometry("600x450")
    image = Image.open('234.png')
    img = ImageTk.PhotoImage(image)
    describe = '智障倉鼠'
    lab0 = Label(root, image = img ,text = describe ,font = ('Arial',20), compound = TOP, bg = '#ccddff')
    
    lab0.pack()
    
    root.mainloop()
    
