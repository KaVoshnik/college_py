import requests
from decimal import Decimal, getcontext

getcontext().prec = 6

def convert_currency(amount:Decimal, rate_from: Decimal, rate_to: Decimal) -> Decimal:
    if amount <= 0:
        raise ValueError("Sum must be positive.")
    return (amount/rate_from)*rate_to