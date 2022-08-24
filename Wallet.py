from uuid import uuid4

import  DB_Scratch, App, User


class Wallet:
    def __init__(self, user: User, wallet_name: str, balance=0, id=uuid4()):
        self.id = id
        self.balance = balance
        self.wallet_name = wallet_name
        self.user = user

    def add_bill(self, bill):
        App.Application.db.add_bill_db(bill)

    def get_user_by_wallet(self):
        return self.user

    def __str__(self):
        return 'This is ' + self.wallet_name + ' wallet'
