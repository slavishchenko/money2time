from input_validation import is_int, is_valid_input


class Item:
    """ Initialize the class with item name and item price"""


    def __init__(self, name:str, price:int) -> None:
        self.name = name
        self.price = price


    @classmethod
    def get(cls):
        item_name = input('What do you want to buy? (Required):\n')
        if item_name and not is_int(item_name):
            item_price = input('How much does it cost? (Required):\n')
            if is_valid_input(item_price):
                return cls(item_name, int(item_price))
        return False
