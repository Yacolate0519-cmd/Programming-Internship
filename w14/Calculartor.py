from tkinter import *

def clear():
    progress.set('')
    preview.delete(0, 'end')  # 修正了 Entry 的操作方法

def pressButton(button):
    if button == '=':
        try:
            result = eval(preview.get())  # 將 `get` 加上括號以正確調用
            preview.delete(0, END)
            preview.insert(END, str(result))
        except Exception as e:
            preview.delete(0, END)
            preview.insert(END, 'Error')
    elif button == 'C':
        preview.delete(0, END)
    else:
        preview.insert(END, button)

# 主視窗
root = Tk()
root.title('計算機')
root.geometry('400x600')

# 進度顯示
progress = StringVar()
progress.set('')

Label(root, textvariable=progress).grid(row=0, column=0, columnspan=4)
preview = Entry(root, textvariable=progress, justify=RIGHT, font=('Arial', 20))
preview.grid(row=1, column=0, columnspan=4)

# 按鈕配置
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '.', '+',
    '='
]

# 動態生成按鈕
row = 3
col = 0
for i, button in enumerate(buttons):
    Button(
        root,
        text=button,
        font=('Arial', 20, 'bold'),
        command=lambda b=button: pressButton(b)
    ).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
    
    col += 1
    if col > 3:  # 每行放置 4 個按鈕
        col = 0
        row += 1

root.mainloop()