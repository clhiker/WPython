from tkinter import*

window = Tk()
window.title("Label")
lab = Label(window, text = "Print", bg = "blue", fg = "red")
lab.grid(padx=100 , pady=15)

window.mainloop()