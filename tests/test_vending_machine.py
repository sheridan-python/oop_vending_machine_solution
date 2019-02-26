import pytest

from models import money
from models.vending_machine import VendingMachine


def test_invalid_coin_value():
    """
    Given a string, the insert coin function should raise a ValueError.
    """
    machine = VendingMachine()
    with pytest.raises(ValueError):
        machine.insert_coin('5')


def test_insert_quarter():
    """
    Given a quarter, no error should be raised.
    """
    machine = VendingMachine()
    machine.insert_coin(money.Quarter())


def test_insert_five_cents():
    """
    Given a five cent coin, no error should be raised.
    """
    machine = VendingMachine()
    machine.insert_coin(money.FiveCent())


def test_insert_ten_cents():
    """
    Given a ten cent coin, no error should be raised.
    """
    machine = VendingMachine()
    machine.insert_coin(money.TenCent())


def test_insert_loonie():
    """
    Given a loonie, no error should be raised.
    """
    machine = VendingMachine()
    machine.insert_coin(money.Loonie())
