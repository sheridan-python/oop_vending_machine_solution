"""
Contains vending machine model.
"""
from .import money


class VendingMachine:
    def __init__(self):
        self.inserted_coins = []

    def insert_coin(self, coin):
        if not isinstance(coin, money.Coin):
            raise ValueError()

        self.inserted_coins.append(coin)
