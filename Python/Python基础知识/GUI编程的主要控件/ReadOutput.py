from tkinter import*

window = Tk()
window.title("ReadOnlyEntry")
conOfenOutput = StringVar()
OnlyEntry = Entry(window, width = 20,state = "readonly",textvariable = conOfenOutput)
OnlyEntry.grid(padx=100 , pady=15)
conOfenOutput.set("lihuizhizhang")
window.mainloop()