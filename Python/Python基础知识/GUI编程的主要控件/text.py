from tkinter import*

window = Tk()
window.title("Text")
text = Text(window, height=10, bg="blue", fg="red")
text.insert(INSERT, 'gyiik')
window.mainloop()