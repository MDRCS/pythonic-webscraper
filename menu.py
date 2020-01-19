import logging
from async_app import books,parser
#from app import books,parser

logger = logging.getLogger('scraping.menu')


USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'q' to exit
Enter your choice: '''


user_choices = {
    'b': parser.ten_best_books,
    'c': parser.cheapest_books,
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        logger.debug('User did not choose to exit program.')
        if user_input in ('b', 'c'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')

menu()