import aiohttp
import asyncio
import time

async def fetch_page(url):
    start = time.time()
    async with aiohttp.ClientSession() as session: #sessions pool
        async with session.get(url) as response:
            print(f'One page load took {time.time() - start} sec')
            return response.status


loop = asyncio.get_event_loop() #Task scheduler
tasks = [fetch_page('http://google.com') for i in range(50)] #create coroutines
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))  #or asyncio.gather(tasks[0],tasks[1],tasks[2],tasks[3] ...) #gather allow to pack the urls as one task
print(f'Total 50 pages took {time.time() - start} sec')

"Concurrency's time execution = almost max(one_page_execution)  "