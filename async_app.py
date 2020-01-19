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
import asyncio
import aiohttp
import async_timeout
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
loop = asyncio.get_event_loop()


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

books = []

start = time.time()
logger.info(f'Going through {parser.number_pages} pages of books...')


async def fetch_page(session,url):
    start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page load took {time.time() - start} sec')
            return await response.text()

async def get_multiple_pages(loop,urls):
    tasks = []
    async with aiohttp.ClientSession(loop = loop) as session:
        for url in urls:
            tasks.append(fetch_page(session,url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = [ f'http://books.toscrape.com/catalogue/page-{page+1}.html' for page in range(1,parser.number_pages) ]

start = time.time()
pages_contents = loop.run_until_complete(get_multiple_pages(loop,urls))
print(f'All pages load took {time.time() - start} sec')


for content in pages_contents:
    parser = allbookspage(content)
    books.extend(parser.books)


# for book in _books:
#     print(book)



















