import pandas

# frc code


# not blank funct
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("sorry this cant be blank. please try again")
        else:
            return response


# answer options (string checker)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")
            continue


# check users enter a number more than zero, has a custom
# error message.  Uses 'type' to accommodate either
# an integer of float
def num_check(question, num_type):
    if num_type == int:
        error = "Please enter an integer that is more than zero"
    else:
        error = "Please enter a number is more than zero"

    while True:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

def currency(X):
    return "${:.2f}".format(X)


def get_expenses(var_fixed):...




# check valid options
yes_no_list = ["yes", "no"]

# set up dictionaries and lists\
item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# have you seen this program?
want_instructions = yes_no("have you seen this program before? ")

if want_instructions == "no":
    print("instructions go here")

product_name = not_blank('product name:')

item_amount = num_check('how many items will you be producing', int)

print("please eneter variable costs below..."
      "enter 'xxx' as item name when done. \n")

item_name = ""
while item_name.lower() != "xxx":

    item_name = not_blank("item name: ")

    if item_name.lower() == "xxx":
        break

    quantity = num_check("quantity:", int)
    how_much = num_check('how much? $', float)
    print()

    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(how_much)

variable_costs_frame = pandas.DataFrame(variable_dict)
variable_costs_frame = variable_costs_frame.set_index('Item')

print(variable_costs_frame)





