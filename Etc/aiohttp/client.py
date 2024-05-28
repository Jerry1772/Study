import time
import asyncio
import aiohttp

url = "http://127.0.0.1:8765/test/"

global_map = {}

# async def make_request(client:aiohttp.ClientSession, idx:int):
#     async with client.get(f"{url}{idx}") as resp:
#         global_map[idx] = await resp.json()

# async def main():
#     async with aiohttp.ClientSession() as client:
#         start = time.time()
#         tasks = [asyncio.create_task(make_request(client, idx)) for idx in range(100)]
#         await asyncio.gather(*tasks)
#         end = time.time()
#     print(f"sent 100 requests, time consuming: {end-start}")

async def make_request(idx:int):
    async with aiohttp.ClientSession() as client:
        async with client.get(f"{url}{idx}") as resp:
            global_map[idx] = await resp.json()

async def main():
    start = time.time()    
    tasks = [asyncio.create_task(make_request(idx)) for idx in range(100)]
    await asyncio.gather(*tasks)    
    end = time.time()
    print(f'Send 100 requests, time consuming:{end - start}')

if __name__ == "__main__":
    asyncio.run(main())

    print(global_map)