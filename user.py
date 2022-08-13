from input_validation import is_valid_input


class User:
    """ 
    Initialize the class with a monthly salary.
    Optionally specify working hours per day - defaults to 8 -
    and number or workdays in a month - defaults to 22.
    """

    # Default value for working hours per day
    WORKING_HOURS = 8

    # Default value for workdays in a month
    WORKDAYS = 22   

    def __init__(
            self, salary:int, working_hours:int = None,
            workdays:int = None) -> None:
     
        self.salary = salary
        self.working_hours = working_hours
        self.workdays = workdays


    @classmethod
    def get(cls) -> bool:
        salary = input('What\'s your salary? (Required):\n')
        if is_valid_input(salary):
            working_hours = input('Working hours per day? (Press Enter to skip):\n')
            workdays = input('Workdays in a month? (Press Enter to skip):\n')
            if not working_hours and not workdays:
                return cls(int(salary))
            elif is_valid_input(working_hours) and is_valid_input(workdays):
                return cls(int(salary), int(working_hours), int(workdays))
            return False
        return False


    @property
    def daily_wage(self) -> int:
        """Returns daily wage rounded to the nearest whole number"""

        if not self.workdays:
            return round(self.salary / self.WORKDAYS)
        return round(self.salary / self.workdays)


    @property
    def hourly_wage(self) -> int:
        """Returns hourly wage rounded to the nearest whole number"""

        if not self.working_hours:
            return round(self.daily_wage / self.WORKING_HOURS)
        return round(self.daily_wage / self.working_hours)