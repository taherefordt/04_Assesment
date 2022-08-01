from random import choice

def choice_check(question, valid_answer, error):

    # Loop to keep the question going till answered properly
    valid = False
    while not valid:

            response = input(question).lower()
            
            for word in valid_answer:
                if response == word[0] or response == word:
                    return word
            
            print(error)
            print()

yes_no_ans = ["yes", "no"]

valid = False
while not valid:
    yes_no = choice_check("yes or no? ", yes_no_ans, "please answer yes or no")

    if yes_no == "yes" or yes_no == "no":
        print("program continues")

    else:
        print("please enter yes or no")