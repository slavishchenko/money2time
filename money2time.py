from user import User


class Calculator:
    """ 
    Initialize the class with a User object
    """
     
    def __init__(self, user) -> None:
        self.user = user

    def money_to_time(self, price: int) -> dict:
        """
        Takes item price as an argument.
        Calculates how many hours and days you have to work to earn 
        that amount of money.
        Returns dict object with hours and days keys.
        """

        hours = round(price / self.user.hourly_wage)
        if not self.user.working_hours:
            days = round(hours / self.user.WORKING_HOURS)
        else:
            days = round(hours / self.user.working_hours)

        return {'hours':hours, 'days':days}





