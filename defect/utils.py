
# import requests
import aiohttp
import asyncio
import json
import os
import sys


async def post(url, payload):
    print("starting delayed post")
    await asyncio.sleep(2)
    async with aiohttp.ClientSession() as session:
        async with session.put(f'{url}', data=payload) as resp:
            print(resp.status)
            print(await resp.text())


def poster(url, payload):
    try:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(post(url, payload))
    except:
        e = sys.exc_info()[0]
        print(f'Uncaught error = {e}')
        # raise
