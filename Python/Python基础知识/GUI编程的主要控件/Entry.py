from tkinter import*

def change_color(event):
    if ent["fg"] == "blue":
        ent["fg"] = "red"
    else:
        ent["fg"] = "blue"

def con_to_up(event):
    txt.set(txt.get().upper())

window = Tk()
window.title("Entry Widget")
txt = StringVar()
'''ent = Entry(window, width=50, borderwidth=10, bg="light blue", fg="blue", font=10,
                textvariable=txt).grid(row=0, column=1, columnspan=4, padx=5, pady=5)'''
ent = Entry(window,width=30, textvariable=txt, show="g", state=ACTIVE)
ent.grid(padx=75, pady=15)
ent.bind("<Button-3>", con_to_up,change_color)

window.mainloop()