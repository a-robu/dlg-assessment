
import unittest.mock
from unittest.mock import MagicMock
from main import memoized_summation

def test_memoized_summation_once_only():
    ''' test that memoized_summation() calls expensive function only once '''
    mock_internal = MagicMock()
    with unittest.mock.patch('main.sum_numbers_to_add', mock_internal):
        memoized_summation()
        memoized_summation()
        memoized_summation()
        mock_internal.assert_called_once()
