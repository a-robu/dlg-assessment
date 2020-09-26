
import json
import unittest.mock
from unittest.mock import MagicMock
from bottle import response
from boddle import boddle
import main

def test_sum_numbers_to_add():
    ''' test that it actually sums up numbers '''
    assert main.sum_numbers_to_add([1, 2, 3]) == 6

def test_memoized_summation_once_only():
    ''' test that memoized_summation() calls expensive function only once '''
    mock_internal = MagicMock()
    with unittest.mock.patch('main.sum_numbers_to_add', mock_internal):
        main.memoized_summation()
        main.memoized_summation()
        main.memoized_summation()
        mock_internal.assert_called_once()

def test_total_ok_response():
    with boddle():
        with unittest.mock.patch('main.memoized_summation', lambda: 5):
            answer = json.loads(main.total())
        assert answer['total'] == 5
        assert response.status_code == 200

def test_total_error_response():
    ''' check that the api returns a 500 response if an error happens '''
    with boddle():
        with unittest.mock.patch('main.memoized_summation', lambda: 1 / 0):
            answer = json.loads(main.total())
        assert 'error' in answer
        assert response.status_code == 500
