from bs4 import BeautifulSoup
import logging
import re
from Locators.All_books_page_locator import allbookspagelocator
from Pages.book import BookParser

logger = logging.getLogger('scraping.all_books_page')


class allbookspage:


    def __init__(self,content):
        self.soup = BeautifulSoup(content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{allbookspagelocator.BOOKS}`')
        books = self.soup.select(allbookspagelocator.BOOKS)
        return [BookParser(book) for book in books]

    @property
    def number_pages(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(allbookspagelocator.PAGES).text
        logger.info(f'Found number of catalogue pages available: `{content}`')
        num_pages = re.findall('[0-9]+', content)
        logger.info(f'Extracted number of pages as integer: `{num_pages}`.')
        return int(num_pages[1])

    def ten_best_books(self):
        logger.debug('Finding best books by rating...')
        books = self.books
        books = sorted(books, key = lambda book : book.rating, reverse = True)[:5]
        #return books
        for book in books:
            print(book)

    def cheapest_books(self):

        logger.debug('Finding best books by price...')

        books = self.books
        books = sorted(books, key=lambda book: book.price, reverse=False)[:10]
        #return books
        for book in books:
            print(book)


