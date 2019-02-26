"""
Contains all models pertaining to money, coins, etc.
"""
from decimal import Decimal


class DollarAmount(Decimal):
    """
    Represents a dollar amount.

    Extends the decimal.Decimal class.
    """
    def __repr__(self):
        return f"DollarAmount('{self}')"

    def __str__(self):
        return f'${self:,.2f}'


class Coin:
    value = DollarAmount('0')

    def __radd__(self, other):
        return self.value + other


class FiveCent(Coin):
    value = DollarAmount('0.05')


class TenCent(Coin):
    value = DollarAmount('0.10')


class Quarter(Coin):
    value = DollarAmount('0.25')


class Loonie(Coin):
    value = DollarAmount('1')


class Toonie(Coin):
    value = DollarAmount('2')
