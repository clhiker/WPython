from tkinter import*

def chanege_color():
    if btnCalculate["fg"] == "blue":
        btnCalculate["bg"] == "red"
    else:
        btnCalculate["bg"] == "blue"


window = Tk()
window.title("Button")
#png = PhotoImage(file="1.png")
btnCalculate = Button(window, text="1",
                      bg="light blue",
                      #padx=10, pady=10,
                      bd=12, fg="orange",
                      font=6, height=10,
                      highlightcolor="yellow",
                      relief=RAISED,
                      wraplength=8,
                      #image=png,
                      justify=RIGHT, state=ACTIVE, underline=0,
                      activebackground="red", activeforeground="yellow").grid(column=3, row=3, sticky=W)

#btn1.grid(padx=100, pady=150)
#btnCalculate.grid(padx=75, pady=15)

window.mainloop()