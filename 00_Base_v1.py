import random
import time
from operator import add, sub, mul, mod, floordiv, pow

def instructions():
    print()
    print("|+=--         How to play 'Risk of Rain'          --=+|")
    print("|+=--                                             --=+|")
    print("|+=--       1. select a difficulty out of 3       --=+|")
    print("|+=--    'drizzle'     'rainstorm'    'monsoon'   --=+|")
    print("|+=--                                             --=+|")
    print("|+=--   2. choose how many questions to answer    --=+|")
    print("|+=--     answering faster and playing harder     --=+|")
    print("|+=--       difficulties grants more points       --=+|")
    print("|+=--                                             --=+|")
    print("|+=--     3. if you want to quit type 'xxx'       --=+|")
    print("|+=--   and once youve completed the questions    --=+|")
    print("|+=--  you can play again and try to do better    --=+|")
    print("|+=--                                             --=+|")
    print()

def decorator(text, decorator, lines):

    ends = decorator * 4
    statement = "{} {} {}".format(ends, text, ends)
    text_length = len(statement)

    if lines == "3":
        print("|+=--", decorator * text_length, "--=+|" )
        print("|+=--", statement, "--=+|")
        print("|+=--", decorator * text_length, "--=+|" )

    if lines == "1":
        print("|+=--", statement, "--=+|")

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

yes_no = ["yes", "no"]
questions_played = 0

# Valid difficulties
difficulties = ["drizzle", "rainstorm", "monsoon"]

# Ranges for different functions
ADD_RANGE = 50
SUB_RANGE = 50
MULT_RANGE = 10
DIV_RANGE = 10
EXP_RANGE = 4

played_before = choice_check("|+=- Have you played this math quiz before? -=+| ", yes_no, "|+=- Please type yes or no")

if played_before == "no":
    instructions()

# Asks the user what difficulty theyll play
play_again = "yes"
while play_again == "yes":

    difficulty = choice_check("|+=- What difficulty will you choose? drizzle, rainstorm, or monsoon -=+| ", difficulties, "|+=- please choose one of the difficulties listed -=+|")

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

    # Asks user how many questions they want to answer
    questions_total = intcheck("|+=-- How many questions do you want to answer? --+=| ", 1, None, None)
    questions_played = 0
    total_points = 0

    while questions_total > questions_played:

        operator = random.choice(operators)
        questions_played += 1

        # Changes the difficulty multiplier / what operator is printed depending on what operator is used
        if operator == add:
            shown_op = "+" 
            if difficulty == "drizzle":
                diff_multiplier = 10

            elif difficulty == "rainstorm":
                diff_multiplier = 25
            
            else:
                diff_multiplier = 50

        elif operator == sub:
            shown_op = "-"

            if difficulty == "drizzle":
                diff_multiplier = 5

            elif difficulty == "rainstorm":
                diff_multiplier = 12
            
            else:
                diff_multiplier = 25

        elif operator == mul:
            shown_op = "*"

            if difficulty == "rainstorm":
                diff_multiplier = 0.8
            else:
                diff_multiplier = 2.5

        elif operator == floordiv:
            shown_op = "/"

            if difficulty == "rainstorm":
                diff_multiplier = 0.8
            else:
                diff_multiplier = 2.5

        elif operator == mod:
            shown_op = "%"
            if difficulty == "monsoon":
                diff_multiplier = 0.2

        else:
            shown_op = "^"
            if difficulty == "monsoon":
                diff_multiplier = 0.2

        num1, num2 = random.randint(1, 20 * diff_multiplier), random.randint(1, 10 * diff_multiplier)

        #calculates the points awarded
        given_points = 300 * score_coefficient

        # answer for the question
        answer = operator(num1, num2)

        # Starts timer before the question and ends it right after the user answers
        start_time = time.time()
        
        # actual question
        question = "|+=- What is {} {} {}? (type 'xxx' to quit)-=+| \n".format(num1, shown_op, num2)

        # prints the round number
        print("|+=- Round {} of {}: -=+|".format(questions_played, questions_total))

        # asks user the question
        response = intcheck(question, None, None, "xxx")

        # timer stops here
        end_time = time.time()

        # calculates points depending on time taken
        given_points -= 10 *(round((end_time - start_time)))

        # outcomes depending on response
        if response == answer:
            print("|+=- Correct, {} points -=+|\n".format(given_points))
            total_points += given_points
        
        elif response == "xxx":
            break

        else:
            print("|+=- You got it wrong -=+|\n")

    # tells player the total points they earned
    print("|+=- you had {} points when the game finished -=+| \n".format(total_points))

    # asks user if they'll play again
    play_again = choice_check("|+=- do you want to play again? -+=| ", yes_no, "|+=- Please answer yes or no -=+|")