from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=200, pady=200)


def miles_to_kilometer():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    kilometer_result_label.config(text=f"{km}")


# Entery
miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)

window.mainloop()
