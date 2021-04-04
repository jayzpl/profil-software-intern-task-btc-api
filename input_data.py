def is_valid(*args) -> bool:
    """
    Checks if input data are strings
    """
    number_of_valid_data = 0
    for i in args:
        if type(i) == str:
            number_of_valid_data += 1
        else:
            number_of_valid_data -= 1
    if number_of_valid_data == len(args):
        return True
    else:
        return False
