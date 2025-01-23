from tkinter import *
    
if __name__ == '__main__':
    root = Tk()
    root.title("GUI_001")
    root.geometry("500x400+100+50")
    
    label = Label(root,
                    text = 'Yacolate 0519 @gmail.com',
                    anchor = NW,
                    font = ('Time new Roman', 20 , 'italic' ,'bold' , UNDERLINE),
                    width = 30,
                    height = 20,
                    wraplength = 100, 
                    justify = RIGHT,
                    background = '#4ABFC3',
                    foreground = '#ff000f'
                    )
    
    
    label.pack()
    
    root.mainloop()
    
