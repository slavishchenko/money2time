def is_int(value) -> None:
    """ 
    Returns True if value is integer 
    """

    try:
        int(value)
        return True
    except:
        return False


def input_is_not_none(value) -> None:
    """Return True if user has provided input"""

    return True if value else False


def is_valid_input(user_input) -> None:
    """
    Checks whether the user has provided a valid input
    """
    return True if input_is_not_none(user_input) and is_int(user_input) else False
