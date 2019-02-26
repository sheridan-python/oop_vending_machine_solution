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


def test_insert_toonie():
    """
    Given a toonie, no error should be raised.
    """
    machine = VendingMachine()
    machine.insert_coin(money.Toonie())


def test_insert_coins_stores_on_object():
    """
    Given that coins are inserted in to the vending machine,
    they should be stored on the object as a inserted_coins property.
    """
    machine = VendingMachine()
    coins = [money.Toonie(), money.TenCent(), money.FiveCent()]
    for coin in coins:
        machine.insert_coin(coin)

    assert machine.inserted_coins == coins
