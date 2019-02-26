"""
Contains vending machine model.
"""
from .import money


COIN_CLASSES = [
    money.FiveCent,
    money.TenCent,
    money.Quarter,
    money.Loonie,
    money.Toonie
]


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
        coins = []
        balance = self.get_balance()

        for coin_class in COIN_CLASSES:
            if coin_class.value == balance:
                coin = coin_class()  # Create a coin instance
                coins.append(coin)

        return coins
