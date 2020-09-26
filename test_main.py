
import unittest.mock
from unittest.mock import MagicMock
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
