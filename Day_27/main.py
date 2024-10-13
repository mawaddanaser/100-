from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def button_clicked():
    print("I've clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    my_label.grid(column=0, row=0)


# Label

my_label = Label(text="I Am a Label", font=("Arial", 24))
my_label.config(text="New text")
my_label.grid(column=0, row=0)

# Button


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# new_button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=3)

window.mainloop()
