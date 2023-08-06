def string_checker(question, num_letters, valid_responses):
    error = "please choose {}, {}, {}, {}, {} , {} or leave empty if unit not found".format(valid_responses[0],
                                                        valid_responses[1],
                                                        valid_responses[2],
                                                        valid_responses[3],
                                                        valid_responses[4],
                                                        valid_responses[6])








    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == response == item:
                return item

        print(error)

valid_units_list = ["kg", "g", "mg", "l", "ml","","cups"]

while True:


    units = string_checker("please select units (kg , g , mg , l , ml,cups or leave empty if unit not found):", 1,
                           valid_units_list)



    print("you chose", units)
    print()

