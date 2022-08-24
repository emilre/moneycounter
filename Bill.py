import Wallet
from Category import Category
from datetime import datetime
import uuid


class Bill:

    def __init__(self, amount: int or float, name: str, category, wallet: Wallet):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.name = name
        self.date = datetime.now()
        self.category = category
        self.wallet = wallet

    def __str__(self):
        return str(self.amount)
