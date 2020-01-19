import asyncio
import async_timeout
import aiohttp
import time

async def fetch_page(session, url):
    start = time.time()
    async with async_timeout.timeout(10): #if the url doesn't give the content before 10 sec the program will raise an execption
        async with session.get(url) as response:
            print(f'Page load took {time.time() - start } sec')
            return response.status

" we could not using loop get_mutiple_pages(urls) -> aiohttp.ClientSession() -> when the session will be constructed automatically the loop will be created"

async def get_mutiple_pages(loop,urls):
    tasks = []
    async with aiohttp.ClientSession(loop = loop) as session:
        for url in urls:
            tasks.append(fetch_page(session,url)) #create coroutines
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()
urls = ['http://google.com' for i in range(50)]
start = time.time()
loop.run_until_complete(get_mutiple_pages(loop,urls))
print(f'Total pages load took {time.time() - start}')

