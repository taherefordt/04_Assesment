import random
import time
from operator import add, sub, mul, mod, floordiv, pow

def decorator(text, decorator, lines, wanted_len, end1, end2):

    # this line here fills in negative space with decorator
    changed_text = "{} {} {}".format(decorator*(wanted_len-int(len(text)))/2, text, decorator*(wanted_len-int(len(text)))/2)

    statement = "{} {} {}".format(end1, changed_text, end2)
    text_length = len(statement)

    if lines == "3":
        print(end1, decorator * text_length, end2 )
        print(end1, statement, end2)
        print(end1, decorator * text_length, end2 )

    if lines == "1":
        print(end1, statement, end2)

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


questions_played = 0

# Valid difficulties
difficulties = ["drizzle", "rainstorm", "monsoon"]

# Ranges for different functions
ADD_RANGE = 50
SUB_RANGE = 50
MULT_RANGE = 10
DIV_RANGE = 10
EXP_RANGE = 4

# Asks the user what difficulty theyll play
difficulty = choice_check("what difficulty will you choose? \x1b[38;2;170;255;60m drizzle\x1b[37m, \x1b[38;2;255;150;010mrainstorm\x1b[37m, or\x1b[38;2;200;000;000m monsoon\x1b[37m \n", difficulties, "please choose one of the difficulties listed")

# Difficulties for functions on 'drizzle'

if difficulty == "drizzle":

    operators = (add, sub)

    score_coefficient = 0.5

# Difficulties for functions on 'rainstorm'

elif difficulty == "rainstorm":

    operators = (add, sub, mul, floordiv)

    score_coefficient = 1

# Difficulties for different functions on 'monsoon'

elif difficulty == "monsoon":

    operators = (add, sub, mul, floordiv, mod, pow)

    score_coefficient = 2

questions_total = intcheck("how many questions do you want to answer? ", 1, None, "xxx")

total_points = 0

while questions_total > questions_played:

    operator = random.choice(operators)

    if operator == add:
        shown_op = "+" 
        if difficulty == "drizzle":
            diff_multiplier = 10

        elif difficulty == "rainstorm":
            diff_multiplier = 25
        
        else:
            diff_multiplier = 50

    elif operator == sub:
        shown_opp = "-"

        if difficulty == "drizzle":
            diff_multiplier = 10

        elif difficulty == "rainstorm":
            diff_multiplier = 25
        
        else:
            diff_multiplier = 50

    elif operator == mul:
        shown_op = "*"

        if difficulty == "rainstorm":
            diff_multiplier = 1.7
        else:
            diff_multiplier = 5

    elif operator == floordiv:
        shown_op = "/"

        if difficulty == "rainstorm":
            diff_multiplier = 1.7
        else:
            diff_multiplier = 5

    elif operator == mod:
        shown_op = "%"
        if difficulty == "monsoon":
            diff_multiplier = 2.5

    else:
        shown_op = "^"
        if difficulty == "monsoon":
            diff_multiplier = 0.4

    num1, num2 = random.randint(1, 10 * diff_multiplier), random.randint(1, 10 * diff_multiplier)

    given_points = 300 * score_coefficient

    answer = operator(num1, num2)

    response = intcheck("what is {} {} {}? ".format(num1, shown_op, num2), 1, None, "xxx")



    if response == answer:
        print ("correct", given_points,"points!")
        total_points += given_points

    