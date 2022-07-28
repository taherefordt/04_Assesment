import random
import operator
from operator import add
import time

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

diff_multiplier = 1
score_coefficient = 1
operator = (add)
shown_op = "+"
num1, num2 = random.randint(1, 10 * diff_multiplier), random.randint(1, 10 * diff_multiplier)

given_points = 300 * score_coefficient

answer = operator(num1, num2)

start_time = 0

start_time = time.time()

response = intcheck("what is {} {} {}? ".format(num1, shown_op, num2), 1, None, "xxx")

endtime = time.time()

total_time = endtime - start_time

print(start_time)

