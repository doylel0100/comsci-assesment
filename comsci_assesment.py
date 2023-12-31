import pandas

#funtion starts here
#not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("sorry this cant be blank. please try again")
        else:
            return response

#number checker
def num_check(question, num_type):
    if num_type == int:
        error = "Please enter an integer that is more than zero"


    else:
        error = "Please enter a number that is more than zero and less than 10,000"

    while True:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)

            elif response >= 10000:
                print(error)


            else:
                return response

        except ValueError:
            print(error)

#string checker
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
            if response == item:
                return item

        print(error)

#yes no checker
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





#vailid units
yes_no_list = ["yes", "no"]
valid_units_list = ["kg", "g", "mg", "l", "ml"]
valid_units_list_2 = ["kg", "g", "mg", "l", "ml"]

#variables
ingredient_list = []
quantity_used_list = []
units_list = []
units_v2_list = []
price_list = []
amount_list = []
cost_list = []
cost_ingerdiant_used_list = []

#dictionarys
variable_dict = {
    "Ingrediant ": ingredient_list,
    "Quantity used ": quantity_used_list,
    "Units ": units_list
}

ingredient_purchased_dict = {
    "Price per g/ml": price_list,
    "Amount": amount_list,
    "Cost ": cost_list,
    "Unit ": units_v2_list,
    "Cost of ingrediants used ": cost_ingerdiant_used_list,
    "Ingrediant ": ingredient_list

}

#want instructons
want_instructions = yes_no("do you want to read the instructions? ")
if want_instructions == "yes":
    print("instructions go here")

print()


#dish name
what_dish = not_blank("what dish are you making ")

#serving amount
dish_amount = num_check('how many servings? \n'
                        '', float)

print("please enter variable costs below..."
      "enter 'xxx' as ingrediant name when done. \n")


#ingredient name and exit code
ingredient_name = ""
while ingredient_name.lower() != "xxx":

    ingredient_name = not_blank("ingredient name: ")

    if ingredient_name.lower() == "xxx":
        break

    quantity_used = num_check("quantity used:", float)


#units
    units = string_checker("please select units (kg , g , mg , l , ml):", 1,
                           valid_units_list)
    print(units)







    print()
#amount percahsed and units
    amount_purchased = num_check('amount purchased', float)

    units_purchased = string_checker("please select units (kg , g , l , ml):", 1,
                           valid_units_list_2)
#ingredient cost
    ingredient_cost = num_check('ingredient cost $', float)
    print()
#cost per unit
    cost_per_unit = cost_per_unit_calc(amount_purchased, units_purchased,ingredient_cost)
    print("amount purchased", amount_purchased)
    print("units", units)
    print("ingredient cost", ingredient_cost)
    print("cost per unit", cost_per_unit)

#cost per ingrediant
    cost_per_ingredient = (cost_per_unit * quantity_used)
    print("ingredient cost", cost_per_ingredient)

#adding columns to the table
    ingredient_list.append(ingredient_name)
    quantity_used_list.append(quantity_used)
    units_list.append(units)
    units_v2_list.append(units_purchased)
    amount_list.append(amount_purchased)
    cost_list.append(ingredient_cost)
    price_list.append(cost_per_unit)
    cost_ingerdiant_used_list.append(cost_per_ingredient)

#printing infromation for table
print()
print("name of dish: ", what_dish)
print()
print("number of servings: ", dish_amount)
print()
variable_costs_frame = pandas.DataFrame(variable_dict)
variable_costs_frame = variable_costs_frame.set_index('Ingrediant ')

print(variable_costs_frame)
print()

ingredient_costs_frame = pandas.DataFrame(ingredient_purchased_dict)
ingredient_costs_frame = ingredient_costs_frame.set_index('Price per g/ml')

print(ingredient_costs_frame)

total_ingredient_cost = ingredient_costs_frame['Cost of ingrediants used '].sum()

cost_per_serving = (total_ingredient_cost / dish_amount)
print()
print("Total cost", total_ingredient_cost)
print()
print("Cost per serving", cost_per_serving)