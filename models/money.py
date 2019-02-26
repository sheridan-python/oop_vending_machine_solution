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
    """Base class representing coins."""
    value = DollarAmount('0')

    def __radd__(self, other):
        return self.value + other

    def __eq__(self, other):
        return self.value == other.value


class FiveCent(Coin):
    """5 cent coin."""
    value = DollarAmount('0.05')


class TenCent(Coin):
    """10 cent coin."""
    value = DollarAmount('0.10')


class Quarter(Coin):
    """25 cent coin."""
    value = DollarAmount('0.25')


class Loonie(Coin):
    """$1 coin."""
    value = DollarAmount('1')


class Toonie(Coin):
    """$2 coin."""
    value = DollarAmount('2')
