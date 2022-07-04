# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code=None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            bound = "both"
        elif low is not None:
            bound = "low"
        elif high is not None:
            bound = "high"
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
            if bound == "low" and response < low:
                print(error)
                continue

            # Checks response is not too high
            if bound == "high" and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue
