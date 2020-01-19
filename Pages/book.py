import re
import logging
from Locators.book_locators import booklocator

logger = logging.getLogger('scraping.book_parser')

class BookParser:


    RATING = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self,parent):
        logger.debug(f'New book parser created from `{parent}`')
        self.parent = parent

    def __repr__(self):
        return f'{self.name}, ${self.price} ({self.rating}  star)'

    @property
    def name(self):
        logger.debug('Finding book name...')
        name = self.parent.select_one(booklocator.NAME).attrs['title']
        logger.info(f'Found book name, `{name}`.')
        return name

    @property
    def link(self):
        logger.debug('Finding book page link...')
        link = self.parent.select_one(booklocator.LINK).attrs['href']
        logger.info(f'Found book page link, `{link}`.')
        return link

    @property
    def price(self):
        logger.debug('Finding book price...')
        price = self.parent.select_one(booklocator.PRICE).text
        logger.debug(f'Item price element found, `{price}`')
        expr = '[0-9\.]+'
        price = re.findall(expr, price)
        logger.info(f'Found book price, `{price}`.')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        classes = self.parent.select_one(booklocator.RATING).attrs['class']
        logger.debug(f'Found rating class, `{classes}`.')
        logger.debug('Converting to integer for sorting.')
        rating = BookParser.RATING[classes[1]]
        logger.info(f'Found book rating, `{rating}`.')
        return rating

