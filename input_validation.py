def is_int(value) -> bool:
    """ 
    Returns True if value is integer 
    """

    try:
        int(value)
        return True
    except:
        return False


def input_is_not_none(value) -> bool:
    """Return True if user has provided input"""

    return True if value else False

def is_positive_number(value):
    return True if int(value) > 0 else False

def is_valid_input(user_input) -> bool:
    """
    Checks whether the user has provided a valid input
    """
    return True if (
        input_is_not_none(user_input)
        and is_int(user_input)
        and is_positive_number(user_input)
        and int(user_input) != 0
    ) else False
