from tkinter import BOTH


def decorator(text, decorator, lines, wanted_length, left_end = None, right_end = None):

    # Multiplies the number of decorators on the sides until youve reached the desired length
    added_end = wanted_length - len(text)

    # Adds the right amount of decorators to the sides
    ends = decorator * added_end
    statement = "{} {} {}".format(ends, text, ends)

    # Finds length of the text for lines below
    text_length = len(statement)

    # If I want 3 lines it will decorate accordingly
    if lines == "3":
        print(left_end, decorator * text_length, right_end )
        print(left_end, statement, right_end)
        print(left_end, decorator * text_length, right_end )

    # Same here but 1 line
    if lines == "1":
        print(left_end, statement, right_end)




decorator("Welcome to my game", "=", "3", 20,"", "")