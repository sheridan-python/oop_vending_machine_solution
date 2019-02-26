import pytest

from models.vending_machine import VendingMachine


def test_invalid_coin_value():
    machine = VendingMachine()
    with pytest.raises(ValueError):
        machine.insert_coin('5')
