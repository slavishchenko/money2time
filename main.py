import sys
import os
import time

from user import User
from item import Item


def main() -> None:
    print('Press CTRL + C to quit.\n')

    user = User.get()
    if user:
        item = Item.get()
        if item:
            hours_to_work, days_to_work = user.money_to_time(item.price).values()
            print(f'In order to afford {item.name}, you need to work:')
            if days_to_work >= 1:
                print(f'{hours_to_work} hours; That amounts to {days_to_work} day(s) in total.')
            else:
                print(f'{hours_to_work} hours.')
        else:
            print('Invalid input!')
            main()
    else:
        print('Invalid input!')
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting..')
        time.sleep(.1)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)