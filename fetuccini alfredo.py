import pandas

def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("sorry this cant be blank. please try again")
        else:
            return response


def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an intager ")


def string_checker(question, num_letters, valid_responses):
    error = "please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2
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