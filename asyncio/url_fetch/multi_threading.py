import requests
from concurrent import futures
import logging


def fetch_url(url: str):

    try:
        resp = requests.get(url)

    except Exception as e:
        logging.info(f'Error fetching: {url}')

    else:
        return resp.content
        

def fetch_all(urls: list):

    with futures.ThreadPoolExecutor() as executor:

        responses = executor.map(fetch_url, urls)

    return responses
