import pytest

from simple_functions import my_sum, factorial


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        iterable = [1, 2, 3]
        expected = 6
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('iterable, expected', [
        (5, 120),
        (4, 24)
    ])
    def test_factorial(self, iterable, expected):
        iterable = 5
        expected = 120
        fact = factorial(iterable)
        assert fact == expected
