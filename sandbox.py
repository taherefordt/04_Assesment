import random
import time


def decorator(text, decorator, lines, wanted_len, end1, end2, len_text):


    # this line here calculates amount of decor needed
    added_decor = decorator * round(wanted_len - len(text)/2)

    statement = "{} {} {}".format(end1, text, end2)
    text_length = len(statement)

    if lines == "3":
        print(end1, added_decor, decorator * text_length, added_decor, end2)
        print(statement)
        print(end1, added_decor, decorator * text_length, added_decor, end2)

    if lines == "1":
        print(end1, added_decor, statement, added_decor, end2)


# Choice checking function
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

# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code=None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

# Valid difficulties
difficulties = ["drizzle", "rainstorm", "monsoon"]

difficulty_question = decorator("what difficulty will you choose? \x1b[38;2;170;255;60m drizzle\x1b[37m, \x1b[38;2;255;150;010mrainstorm\x1b[37m, or\x1b[38;2;200;000;000m monsoon\x1b[37m", "=", "3", 100, "|+=-", "-=+|")
# Asks the user what difficulty theyll play
difficulty = choice_check(difficulty_question, difficulties, "please choose one of the difficulties listed")

