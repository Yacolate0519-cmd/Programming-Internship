from tkinter import *
    
if __name__ == '__main__':
    root = Tk()
    root.title("GUI_001")
    root.geometry("500x400+100+50")
    
    bitmap = ['error','info','question']
    bg = ['#ff0000','#00ff00','#0000ff']
    compound = [LEFT , RIGHT , TOP]
    reliefs = [FLAT , GROOVE , RIDGE]
    text = 'ischool AITA'
    
    for i in range(len(bitmap)):
        label = Label(root,
                      bitmap = bitmap[i],
                      bg = bg[i],
                      text = text,
                      compound = compound[i],
                      relief = reliefs[i]
                      )
        label.pack(padx = 10 , pady = 5)
        
    # label = Label(root,
    #               bg = '#ff0000',
    #               bitmap = 'error',
    #               text = 'ischool AITA',
    #               compound=LEFT
    #               ).pack()
    # label = Label(root,
    #               bitmap = 'info',
    #               bg = '#00ff00',
    #               text = 'ischool AITA',
    #               compound = RIGHT).pack()
    # label = Label(root,
    #               bitmap = 'question',
    #               text = 'ischool AITA',
    #               bg = '#0000ff',
    #               compound = TOP)
    
    label.pack()
    
    root.mainloop()