import tkinter

window = tkinter.Tk()
window.title("Tkinter GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)


window.mainloop()