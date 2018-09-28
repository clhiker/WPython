from tkinter import *

'''class Calculate:
    def __init__(self, infor=""):
        self._infor = infor'''

def getinfor():
    infor = "1"
    return infor

def entry(window):
    txt = StringVar()
    L1 = Label(window, text="Enter Number",
               bg="light blue", fg="red", font=10).grid(row=0, column=0)
    L2 = Label(window, width=50, height=1, font=10, borderwidth=5,
               bg="light blue", fg="blue").grid(row=0, column=1, columnspan=4, padx=5, pady=5)

    '''text = Text(window, width=50, height=1, font=10,borderwidth=5,
                bg="light blue", fg="blue").grid(row=0, column=1, columnspan=4, padx=5, pady=5)'''
    t = Text(window)
    t.insert(END, "hhda")

def button(window):

    btn1 = Button(window, text="1", bg="light blue",
                  padx=10, pady=10, bd=12, font=10,
                  activebackground="red", activeforeground="yellow", command=getinfor).grid(row=1, column=0)
    btn2 = Button(window, text="2", bg="light blue",
                  padx=10, pady=10, bd=12, font=10,
                  activebackground="red", activeforeground="yellow").grid(row=1, column=1)
    btn3 = Button(window, text="2", bg="light blue",
                  padx=10, pady=10, bd=12, font=10,
                  activebackground="red", activeforeground="yellow").grid(row=1, column=2)
    btnDec = Button(window, text="2", bg="light blue",
                  padx=10, pady=10, bd=12, font=10,
                  activebackground="red", activeforeground="yellow").grid(row=1, column=3)
    btnDec = Button(window, text="2", bg="light blue",
                    padx=10, pady=10, bd=12, font=10,
                    activebackground="red", activeforeground="yellow").grid(row=2, column=3)

def main():
    window = Tk()
    window.title("Calculate")
    window.minsize(400, 500)
    entry(window)
    button(window)
    window.mainloop()

main()






'''btn2 = Button(window, text = "", bg = "light blue")
btn3 = Button(window, text = "", bg = "red")
btn4 = Button(window, text = "", bg = "light blue")
btn5 = Button(window, text = "", bg = "light blue")
btn6 = Button(window, text = "", bg = "light blue")
btn7 = Button(window, text = "", bg = "light blue")
btn8 = Button(window, text = "", bg = "light blue")
btn9 = Button(window, text = "", bg = "light blue")
btn0 = Button(window, text = "", bg = "light blue")'''


'''btn2.grid(padx=75, pady=15)
btn3.grid(padx=75, pady=15)
btn4.grid(padx=75, pady=15)
btn5.grid(padx=75, pady=15)
btn6.grid(padx=75, pady=15)
btn7.grid(padx=75, pady=15)
btn8.grid(padx=75, pady=15)
btn9.grid(padx=75, pady=15)
btn0.grid(padx=75, pady=15)'''

