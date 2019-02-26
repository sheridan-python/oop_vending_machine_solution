"""
Contains vending machine model.
"""
from .import money


class VendingMachine:
    def insert_coin(self, coin):
        if not isinstance(coin, money.Coin):
            raise ValueError()

        return
