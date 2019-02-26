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


def test_get_balance_returns_the_sum_of_inserted_coins():
    """
    Given each type of coin is inserted, a dollar amount of 3.40
    should be returned.
    """
    machine = VendingMachine()
    machine.insert_coin(money.Toonie())
    machine.insert_coin(money.Loonie())
    machine.insert_coin(money.Quarter())
    machine.insert_coin(money.TenCent())
    machine.insert_coin(money.FiveCent())

    assert machine.get_balance() == money.DollarAmount('3.40')


def test_get_change_when_nothing_inserted():
    machine = VendingMachine()
    assert machine.get_change() == []


def test_get_change_when_balance_is_25_cents():
    machine = VendingMachine()
    machine.insert_coin(money.Quarter())

    assert machine.get_change() == [money.Quarter()]


def test_get_change_when_balance_is_one_dollar():
    """
    Given a balance of $1, a loonie should be returned.
    """
    machine = VendingMachine()
    for _ in range(4):  # Repeat 4 times
        machine.insert_coin(money.Quarter())

    assert machine.get_change() == [money.Loonie()]


def test_get_change_balance_is_all_coins():
    machine = VendingMachine()
    coins = [
        money.Toonie(),
        money.Loonie(),
        money.Quarter(),
        money.TenCent(),
        money.FiveCent()
    ]
    for coin in coins:
        machine.insert_coin(coin)

    assert machine.get_change() == coins


def test_get_change_balance_is_multiple_coins():
    machine = VendingMachine()
    coins = [
        money.Loonie(),
        money.Quarter(),
        money.Quarter(),
        money.TenCent(),
        money.TenCent()
    ]

    for coin in coins:
        machine.insert_coin(coin)

    assert machine.get_change() == coins


def test_a_balance_that_is_not_a_multiple_of_five():
    class OneCent(money.Coin):
        value = money.DollarAmount('0.01')

    machine = VendingMachine()
    machine.insert_coin(OneCent())

    assert machine.get_change() == []
