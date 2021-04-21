'''
A simple script to compare multi threading with asyncio in a high I/O task.
It is fetching the same url, which points to an image (or whatever you wish),
both with multi threading and with asyncio.
'''

from timeit import default_timer
import asyncio
from prettytable import PrettyTable

from multi_threading import fetch_all
from async_io import fetch_async


if __name__ == '__main__':

    # Table header.
    t = PrettyTable(['Request Count', 'Multithreading', 'AsyncIO', 'Difference', 'Winner'])

    # Insert your URL.
    url = "***"

    # How many times to download.
    indexes = [1, 10, 100, 500, 1000]

    for i in indexes:

        urls = [url] * i

        start = default_timer()        

        responses = fetch_all(urls)

        # Elapsed time.
        delta_multi = default_timer() - start

        start = default_timer()        

        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(loop, i, url))
        loop.run_until_complete(future)
        responses = future.result()

        # Elapsed time.
        delta_async = default_timer() - start

        # Difference between the two ways.
        diff = delta_multi - delta_async

        faster = 'AsyncIO'
        if delta_multi < delta_async:
            faster = 'Multithreading'

        # Add table row.
        t.add_row([i, delta_multi, delta_async, abs(diff), faster])
        
    # Print table.
    print(t)
