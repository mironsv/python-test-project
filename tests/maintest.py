import unittest
from unittest.mock import MagicMock

from exchange_interface import ExchangeInterface
from main import send_order_with_amount


def args_based_return(*args, **kwargs):
    if args[0] == 10:
        return "20"
    elif args[0] == 20:
        return "40"
    else:
        return Exception("exception occurred")


def arg_calculate_return(*args, **kwargs):
    return args[0] * 3


class TestStringMethods(unittest.TestCase):

    def test_parametrized_mock(self):
        my_mock = ExchangeInterface('binance')
        my_mock.send_order = MagicMock(side_effect=args_based_return)
        assert send_order_with_amount(my_mock, 10) == "20 is sent to binance"
        assert send_order_with_amount(my_mock, 20) == "40 is sent to binance"
        assert send_order_with_amount(my_mock, 30) == "exception occurred is sent to binance"

    def test_calculate_mock(self):
        my_mock = ExchangeInterface('binance')
        my_mock.send_order = MagicMock(side_effect=arg_calculate_return)
        assert send_order_with_amount(my_mock, 10) == "30 is sent to binance"
        assert send_order_with_amount(my_mock, 20) == "60 is sent to binance"
        assert send_order_with_amount(my_mock, 30) == "90 is sent to binance"
