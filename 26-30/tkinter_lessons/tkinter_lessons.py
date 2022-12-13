from tkinter import *

window = Tk()
window.title("Tkinter GUI Program")
window.minsize(width=500, height=300)
window.config(padx=2, pady=2)



def button_clicked():
	print("I got clicked")
	input_text = input_element.get()
	label.config(text=input_text)

# Labels
label = Label(text="I am a label", font=("Arial", 24, "bold"))
#label.pack(expand=True)
label.grid(column=0, row=0)


# my_label["text"] = "New Text"
# my_label.config(text="New text via config")


# Buttons
button = Button(text="Click Me", command=button_clicked)
# button.pack()
# button.place(x=0, y=100)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entries
input_element = Entry(width=10)
input_element.grid(column=3, row=3)


window.mainloop()