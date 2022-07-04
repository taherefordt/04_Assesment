def decorator(decorator, lines, wanted_length, left_end, right_end, text, text2=None,):

    # Multiplies the number of decorators on the sides until youve reached the desired length
    added_end = wanted_length - float(len(text))/2
    
    # Adds the right amount of decorators to the sides
    ends = decorator * int(added_end)
    statement = "{} {} {}".format(ends, text, ends)
    if text2 is not None:

        added_end2 = wanted_length - float(len(text2))/2

        if int(added_end2) % 2 != 0:
            int(added_end2) + 1
        else:
            int(added_end2) + 0

        
        ends2 = decorator * int(added_end2)
        statement2 = "{} {} {}".format(ends2, text2, ends2)

    # Finds length of the text for lines below
    text_length = len(statement)

    # If I want 3 lines it will decorate accordingly
    if lines == 4:

        print(left_end, decorator * text_length, right_end )
        print(left_end, statement, right_end)
        print(left_end, statement2, right_end)
        print(left_end, decorator * text_length, right_end )
        
    elif lines == 3:
        print(left_end, decorator * text_length, right_end )
        print(left_end, statement, right_end)
        print(left_end, decorator * text_length, right_end )

    # Same here but 1 line
    elif lines == 1:
        print(left_end, statement, right_end)
