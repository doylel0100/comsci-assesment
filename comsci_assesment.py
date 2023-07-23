import pandas

def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("sorry this cant be blank. please try again")
        else:
            return response


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

def string_checker(question, num_letters, valid_responses):
    error = "please choose {}, {}, {}, {} or {}".format(valid_responses[0],
                                            valid_responses[1],
                                            valid_responses[2],
                                            valid_responses[3],
                                            valid_responses[4])

    if num_letters == 1:
        short_version = 1
    elif num_letters == 2:
        pass






    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)

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

# unit converter
def cost_per_unit_calc(amount_purchased, units, ingredient_cost):
    if units == "kg":
        converted_amount = amount_purchased * 1000
    elif units == "g":
        converted_amount = amount_purchased
    elif units == "mg":
        converted_amount = amount_purchased / 1000
    elif units == "l":
        converted_amount = amount_purchased * 1000
    elif units == "ml":
        converted_amount = amount_purchased

    cost_per_unit = ingredient_cost / converted_amount
    return cost_per_unit


yes_no_list = ["yes","no"]
valid_units_list = ["kg","g","mg","l","ml"]



ingredient_list = []
quantity_used_list = []
units_list = []
price_list = []
amount_list = []
cost_list = []

variable_dict = {
    "ingrediant": ingredient_list,
    "Quantity used ": quantity_used_list,
    "units": units_list
}

ingredient_purchased_dict = {
"price": price_list,
"amount": amount_list,
"unit": units_list,
"cost": cost_list
}
want_instructions = yes_no("do you want to read the instructions? ")
if want_instructions == "yes":
    print("instructions go here")


print ()



what_dish = not_blank("what dish are you making ")

dish_amount = num_check('how many servings'
                        '', int)


print("please enter variable costs below..."
      "enter 'xxx' as ingrediant name when done. \n")

ingredient_name = ""
while ingredient_name.lower() != "xxx":

    ingredient_name = not_blank("ingredient name: ")

    if ingredient_name.lower() == "xxx":
        break

    quantity_used = num_check("quantity used:", int)

    units = string_checker("please select units (kg , g , mg , l , ml):", 1 ,
                           valid_units_list)
    print()





    amount_purchased = num_check('amount purchased', int)

    units = string_checker("please select units (kg , g , mg , l , ml):", 1 ,
                           valid_units_list)

    ingredient_cost = num_check('ingredient cost $', float)
    print()

    cost_per_unit = cost_per_unit_calc(amount_purchased, units, ingredient_cost)
   

    cost_per_ingredient = (cost_per_unit * quantity_used)






    ingredient_list.append(ingredient_name)
    quantity_used_list.append(quantity_used)
    units_list.append(units)
    amount_list.append(amount_purchased)
    cost_list.append(ingredient_cost)
    price_list.append(cost_per_unit)


print()
variable_costs_frame = pandas.DataFrame(variable_dict)
variable_costs_frame = variable_costs_frame.set_index('ingrediant')

print(variable_costs_frame)
print ()

ingredient_costs_frame = pandas.DataFrame(ingredient_purchased_dict)
ingredient_costs_frame = ingredient_costs_frame.set_index('price')

print(ingredient_costs_frame)



total_ingredient_cost = ingredient_costs_frame['cost'].sum()

cost_per_serving = (total_ingredient_cost / dish_amount)
print()
print ("cost per serving", cost_per_serving)