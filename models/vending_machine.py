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

    def get_balance(self):
        return sum(self.inserted_coins)

    def get_change(self):
        return self.inserted_coins
