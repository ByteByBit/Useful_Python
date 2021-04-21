import asyncio
from aiohttp import ClientSession, ClientResponseError
import logging


async def fetch(session, url: str):

    try:

        async with session.get(url, timeout=15) as response:
            resp = await response.read()

    except ClientResponseError as e:
        logging.warning(e.code)

    except asyncio.TimeoutError:
        logging.warning('Request timed out.')

    except Exception as e:
        logging.warning(e)

    else:
        return resp

    return None


async def fetch_async(loop, r: int, url: str):

    tasks = []
    # One client session.
    async with ClientSession() as session:

        for i in range(r):
            
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)

        # Await outside the loop.
        responses = await asyncio.gather(*tasks)

    return responses
