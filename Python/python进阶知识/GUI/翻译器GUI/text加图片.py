from tkinter import *

root = Tk()

root.title('翻译器')
root.geometry('600x500')  # 窗口大小
root.resizable(width=True, height=True)  # 宽和高都设置为可变的
input_text = Text(root,
                 background='lavender',
                 #borderwidth=30,
                 font=('Helvetica',12,'bold'),
                 foreground='red',
                 highlightbackground='yellow',# highlightcolor='yellow',
                 highlightthickness=4,
                 insertbackground='blue',#insertborderwidth=10
                 relief='sunken',
                 width=25,
                 )
input_text.grid(row=4,column=0)
imag = PhotoImage(file='D://test/404.gif')
input_text.image_create(END,image=imag)

root.mainloop()