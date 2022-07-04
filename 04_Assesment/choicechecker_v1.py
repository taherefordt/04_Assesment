
def choice_check(question, valid_answer, error):

    # Loop to keep the question going till answered properly
    valid = False
    while not valid:

            response = input(question).lower()
            
            # If the input is the first letter, or the whole word of a valid answer it will accept it as a valid answer
            for word in valid_answer:
                if response == word[0] or response == word:
                    return word
            
            # If the response is invalid it will print an error and repeat the question
            print(error)
            print()