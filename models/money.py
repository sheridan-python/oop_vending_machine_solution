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
    pass


class FiveCent(Coin):
    pass


class TenCent(Coin):
    pass


class Quarter(Coin):
    pass


class Loonie(Coin):
    pass


class Toonie(Coin):
    pass
