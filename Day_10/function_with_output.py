# function with oi\utput
def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())


format_name("mawadda", "MAWADDA")


###########

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")


format_name("muhammed", "SAIF")


##################

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    # formated_f_name and formated_l_name becomes output of function by return
    return f"{formated_f_name} {formated_l_name}"


# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing calling function which have the value of parameter(argument)
print(format_name("MeNNa", "nASSer"))
##############

# Already used functions with outputs.
length = len(formatted_name)


#####################

# Return as an early exit
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
