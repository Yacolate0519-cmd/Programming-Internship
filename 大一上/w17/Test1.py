from tkinter import *

# 创建主窗口
root = Tk()
root.title('User Login')
root.geometry('400x300')
root.configure(bg='#f0f0f0')  # 背景颜色

# 调整行列权重
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

# 字体样式
LABEL_FONT = ('Arial', 16, 'bold')
BUTTON_FONT = ('Arial', 14, 'bold')

# 创建标签和输入框
Label(root, text="帳號", font=LABEL_FONT, bg='#f0f0f0').grid(row=0, column=0, sticky=E, padx=10, pady=10)
account_entry = Entry(root, font=('Arial', 14))
account_entry.grid(row=0, column=1, sticky=W, padx=10, pady=10)

Label(root, text="密碼", font=LABEL_FONT, bg='#f0f0f0').grid(row=1, column=0, sticky=E, padx=10, pady=10)
password_entry = Entry(root, font=('Arial', 14), show="*")
password_entry.grid(row=1, column=1, sticky=W, padx=10, pady=10)

# 创建按钮
Button(root, text="Log In", font=BUTTON_FONT, bg='#007BFF', fg='white', width=10, command=lambda: print("Log In")).grid(
    row=2, column=0, columnspan=2, pady=10, ipadx=10, ipady=5
)
Button(root, text="Sign Up", font=BUTTON_FONT, bg='#28A745', fg='white', width=10, command=lambda: print("Sign Up")).grid(
    row=3, column=0, columnspan=2, pady=10, ipadx=10, ipady=5
)

root.mainloop()