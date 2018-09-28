from tkinter import*

def get_color(event):
    lb["bg"] = lb.get(lb.curselection())

def set_color(event):
    lb["fg"] = lb.get(lb.curselection())

def sort_color(event):
    L.sort()
    colorlist.set(tuple(L))

window = Tk()
window.title("Listbox")
L = ["red", "yellow", "light blue", "orange"]
colorlist = StringVar()
lb = Listbox(window,width = 10, height = 5,listvariable = colorlist)
lb.grid(padx=100 , pady=15)
colorlist.set(tuple(L))
#换背景
#lb.bind("<<ListboxSelect>>",get_color)
lb.bind("<<ListboxSelect>>", set_color)
#排序
#lb.bind("<Button-3>", sort_color)
window.mainloop()