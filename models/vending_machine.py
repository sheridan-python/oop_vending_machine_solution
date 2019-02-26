"""
Contains vending machine model.
"""
from .import money


class VendingMachine:
    def insert_coin(self, coin):
        if isinstance(coin, money.Coin):
            return

        raise ValueError()
