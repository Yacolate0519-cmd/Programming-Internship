from tkinter import *
from tkinter import messagebox , filedialog
from PIL import Image , ImageTk

#quitWindow
###########################################################################################################################################
def quitWindow():
    decision = messagebox.askyesno('Worring',
                                   'Quit the window',
                                   icon = messagebox.WARNING)
    if decision == True:
        root.quit()
###########################################################################################################################################


#notePad
##########################################################################################################################################
def notepad():
    if 'internal_frame' in root.children:
        return 
    frame = Frame(root , relief = SOLID)
    frame.grid(row = 0 , column = 0 , sticky = NSEW)

    for i in range(4):
        frame.grid_rowconfigure(i , weight = 1)
        frame.grid_columnconfigure(i , weight = 1)

    text_area = Text(frame , wrap = WORD , font = ('Arial' , 25) , bg = 'lightyellow')
    text_area.grid(row = 0 , column = 0 , sticky = NSEW  , rowspan = 3 ,columnspan = 4)

    style = ('Arial' , 20 , 'bold')

    def open_file():
        file_path = filedialog.askopenfilename(
            filetypes = [('Text files' , '*.txt') , ('All files' , '*.*') , ('Python' , '*.py')]
        )
        if file_path:
            try:
                with open(file_path , 'r') as f:
                    content = f.read()
                    text_area.delete('1.0' , 'end')
                    text_area.insert('1.0' , content)
            except Exception as e:
                messagebox.showerror('Error' , f'Failed to open file: \n{e}')
    
    def save_file():
        file_path = filedialog.asksaveasfilename(
            defaultextension = '.txt',
            filetypes = [('Text files' , '*.txt'),('All files' , '*.*'),('Python' , '*.py')]
        )
        if file_path:
            try:
                with open(file_path , 'w') as f:
                    f.write(text_area.get('1.0' , 'end-lc'))
                messagebox.showinfo('Success' , 'File save successfully')
            except Exception as e:
                messagebox.showerror('Error' , f'Failed to save file: \n{e}')

    def clear():
        text_area.delete('1.0' , 'end')

    oepn = Button(frame , text = 'open' , font = style , command = open_file).grid(row = 3 , column = 0 , sticky = NSEW)
    save = Button(frame , text = 'save' , font = style , command = save_file).grid(row = 3 , column = 1 , sticky = NSEW)
    clear = Button(frame , text = 'clear' , font = style , command = clear).grid(row = 3 , column = 2 , sticky = NSEW)
    close = Button(frame , text = 'close' , font = style , command = frame.destroy).grid(row = 3 , column = 3 , sticky = NSEW)
####################################################################################################################################

#Image View
####################################################################################################################################
def Imgae_View():
    if 'internal_frame' in root.children:
        return 
    frame = Frame(root , relief = SOLID)
    frame.grid(row = 0 , column = 0 , sticky = NSEW)

    for i in range(5):
        frame.grid_rowconfigure(i , weight = 1)
        frame.grid_columnconfigure(i , weight = 1)

    style = ("Arial" , 20 , 'bold')
    global index
    global images

    index = 0
    images = ['1.png','2.png','3.png','4.png']

    #control
    global img
    # image = Image.open(images[1])
    img = ImageTk.PhotoImage(file =  images[index])
    show = Label(frame , image = img , compound = TOP , bg = '#ccddff')
    show.grid(row = 0 , column = 0 , sticky = NSEW , rowspan = 5 ,columnspan = 5)

    def first_image():
        global img , images , index
        index = 0
        img = ImageTk.PhotoImage(file =  images[0])
        show.config(image = img)
        print(index)
    
    def left_image():
        global img , images , index
        index -= 1
        if index < 0:
            index = len(images)
        img = ImageTk.PhotoImage(file =  images[index])
        show.config(image = img)
        print(index)

    def right_image():
        global img , images , index
        index += 1
        if index > len(images) - 1:
            index = 0
        img = ImageTk.PhotoImage(file =  images[index])
        show.config(image = img)
        print(index)

    def last_image():
        global img , images , index
        index = len(images)
        img = ImageTk.PhotoImage(file =  images[-1])
        show.config(image = img)
        print(index)

    first = Button(frame , text = '|<' , font = style , command = first_image).grid(row = 4 , column = 0 , sticky = NSEW)
    left = Button(frame , text = '<' , font = style , command = left_image).grid(row = 4 , column = 1 , sticky = NSEW)
    right = Button(frame , text = '>' , font = style , command = right_image).grid(row = 4 , column = 2 , sticky = NSEW)
    last = Button(frame , text = '>|' ,font = style , command = last_image).grid(row = 4 , column = 3 , sticky = NSEW)
    close = Button(frame , text = 'Close' , command = frame.destroy , font = style).grid(row = 4 , column = 4 , sticky = NSEW)


####################################################################################################################################


if __name__ == '__main__':
    root = Tk()
    root.title('GUI Menu Bar Demo')
    root.geometry('800x800+100+50')

    root.grid_rowconfigure(0 , weight = 1)
    root.grid_columnconfigure(0 , weight = 1)

    menubar = Menu(root)

    tearoff = 0

    #file
    fileMenu = Menu(menubar , tearoff = tearoff)
    menubar.add_cascade(label = 'File' , menu = fileMenu)
    fileMenu.add_command(label = 'Open')
    fileMenu.add_command(label = 'Save')
    fileMenu.add_command(label = 'exit',
                         accelerator = 'Ctrl+E',
                         command = quitWindow)

    #tool
    toolMenu = Menu(menubar , tearoff = tearoff)
    menubar.add_cascade(label = 'Tool' , menu = toolMenu)
    toolMenu.add_command(label = 'NotePad',
                         accelerator = 'Ctrl+1',
                         command = notepad)
    toolMenu.add_command(label = 'Image View',
                         command = Imgae_View)
    toolMenu.add_command(label = 'Simple Calculator')
    
    #game
    gameMenu = Menu(menubar , tearoff = tearoff)
    menubar.add_cascade(label = 'Game' , menu = gameMenu)
    gameMenu.add_command(label = 'Tic Tac Toe')

    #help
    helpMenu = Menu(menubar , tearoff = tearoff)
    menubar.add_cascade(label = 'Help' , menu = helpMenu)
    helpMenu.add_command(label = 'About')

    root.config(menu = menubar)
    root.mainloop()