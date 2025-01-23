from tkinter import *
    
if __name__ == '__main__':
    root = Tk()
    root.title("GUI_001")
    root.geometry("700x400+100+50")
    
    lab00 = Label(root,width = 10,height = 3,bg ='#ccddef',text = '(0,0)',justify = CENTER,font = ('Time new Romen' , 20 , 'bold'))
    lab00.grid(row = 0 , column = 0 , sticky = W , padx = 5 , pady = 3)
                  
    lab01 = Label(root,width = 10,height = 3,bg ='#ffddee',text = '(0,1)',justify = CENTER,font = ('Time new Romen' , 20 , 'bold'))
    lab01.grid(row = 0 , column = 1 , sticky = W , padx = 5 , pady = 3)
                  
    lab02 = Label(root,width = 10,height = 3,bg ='#ccffef',text = '(0,2)',justify = CENTER,font = ('Time new Romen' , 20 , 'bold'))
    lab02.grid(row = 0 , column = 2 , sticky = W , padx = 5 , pady = 3)
                  
    lab03 = Label(root,width = 10,height = 3,bg ='#ccddef',text = '(0,3)',justify = CENTER,font = ('Time new Romen' , 20 , 'bold'))
    lab03.grid(row = 0 , column = 3 , sticky = W , padx = 5 , pady = 3)
                  
    lab04 = Label(root,width = 10,height = 3,bg ='#ccddff',text = '(0,4)',justify = CENTER,font = ('Time new Romen' , 20 , 'bold'))
    lab04.grid(row = 1 , column = 0 , sticky = W , padx = 5 , pady = 3)
                  
    lab05 = Label(root,width = 10,height = 3,bg ='#ccff99',text = '(0,5)',justify = CENTER,font = ('Time new Romen' , 20 , 'bold'))
    lab05.grid(row = 1 , column = 1 , sticky = W , padx = 5 , pady = 3)
    
    root.mainloop()
    
