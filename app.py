""" In this app i will scrape books from a website, simulating operations :
  1- Get books 'Name'
  2- Get books 'Link'
  3- Get books 'Price'
  4- Get books 'Rating'
  5- Get Number of pages on this websites
  6- Get 10 best books
  7- Get the cheapest book

  And also make this operations available for all pages of this websites.
  """

import requests
import time
import logging
from Parser.All_books_page import allbookspage

format = 'format=%(asctime)s | %(levelname)-8s | %(filename)s-%(funcName)s-%(lineno)04d | %(message)s'
logging.basicConfig(
    format=format,
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,  #if we choose to start with the first level (DEBUG) so the logger automatically will display all the others levels
    filename='log.txt' #if we want to write our logs in a file
)

logger = logging.getLogger('scraping')


"Levels that we could output are : ordred by asc \
DEBUG \
INFO \
WARNING \
CRITICAL"

logger.info('Content is loading ...')
url = 'http://books.toscrape.com/'

logger.info('Requesting http://books.toscrape.com')
content = requests.get(url).content

logger.debug('Creating AllBooksPage from page content.')
parser = allbookspage(content)
allbookspage_ = parser.books

_books = []

start = time.time()
logger.info(f'Going through {parser.number_pages} pages of books...')
for page in range(1,parser.number_pages):

    page_start = time.time()
    url = f'http://books.toscrape.com/catalogue/page-{page+1}.html'
    logger.info(f'Requesting {url}')
    content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    parser = allbookspage(content)
    print(f'{url} took {time.time() - page_start} sec')
    _books.extend(parser.books) #add books on others pages inside the list and also make the list flat one dimension that is the role of extend
print(f'Total took {time.time() - start}')

# for book in _books:
#     print(book)

books = _books

















