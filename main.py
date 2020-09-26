#!/usr/bin/env python3

import json
import functools
from bottle import route, run
from backend import numbers_to_add

# The sum of a list of numbers is an unchanging (deterministic)
# quantity which may take a long time to compute. To save on
# computation time, we cache the result of the summation after
# the first request. The following SO answer provides a bit of
# context for the `lru_cache` decorator which we use to cache
# the result in memory.
# https://stackoverflow.com/a/14731729
@functools.lru_cache(maxsize=None)
def memoized_summation():
    return sum(numbers_to_add)

@route('/total')
def total():
    return json.dumps({
        'total': memoized_summation()
    })

if __name__ == '__main__':
    run(host='localhost', port=8080)
