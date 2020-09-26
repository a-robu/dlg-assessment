#!/usr/bin/env python3

import logging
import json
import functools
from bottle import route, run, response
from backend import numbers_to_add

def sum_numbers_to_add(numbers=numbers_to_add):
    return sum(numbers)

@functools.lru_cache(maxsize=None)
def memoized_summation():
    ''' Computes the total amount (which is the core of the API response).
    
    The value is cached in memory after the first invocation.
    '''
    # The sum of a list of numbers is an unchanging (deterministic)
    # quantity which may take a long time to compute. To save on
    # computation time, we cache the result of the summation after
    # the first request. The following SO answer provides a bit of
    # context for the `lru_cache` decorator which we use to cache
    # the result in memory.
    # https://stackoverflow.com/a/14731729
    return sum_numbers_to_add()

@route('/total')
def total():
    status_code = 200
    try:
        answer = {
            'total': memoized_summation()
        }
    except Exception as e:
        # The error catch-all above prevents exceptions from appearing in logs.
        # So, we log the error explicitly.
        logging.error(e, exc_info=True)
        status_code = 500
        # Because no failure outcomes are defined, there is no need to be
        # more specific in the status code other than success/unexpected failure.
        answer = {
            'error': 'An unexpected error occured while preparing the reponse.'
        }
    response.status = status_code
    response.set_header('Content-Type', 'application/json')
    return json.dumps(answer)

if __name__ == '__main__':
    run(host='localhost', port=8080)
