from tkinter import*

window = Tk()
window.title("Scrollbar")
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(padx=100, pady=15)

window.mainloop()