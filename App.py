import User
import Wallet
import Bill

import Menu
# Переделать под базу
# Начать смотреть джанго
from DB_Scratch import DataBase


class Application:
    db = DataBase('DB')

    @staticmethod
    def login(login: str, password: str):
        if login.isalnum():
            if 4< len(login) < 18:
                return Application.db.login_db(login, password)
            return "Login : Your login has to be shorter or longer 4-18"
        return "Login : Numbers and Letters only !"

    @staticmethod
    def add_wallet(wallet):
        return Application.db.add_wallet_db(wallet)
    @staticmethod
    def add_bill(bill):
        return Application.db.add_bill_db(bill)
    @staticmethod
    def update_balance(Bill):
        pass
    @staticmethod
    def register(name: str, surname: str, login: str, password: str):
        temp_user = User.User(name, surname, login, password)
        if temp_user.login.isalnum():
            if 4 < len(temp_user.login) < 18:
                return Application.db.add_user_db(temp_user)
            return "Login : Your login has to be shorter or longer 4-18"
        return "Login : Numbers and Letters only !"

    @staticmethod
    def show_all_wallet_of_user(user):
        wallet = Application.db.show_wallets_of_user(user)
        if wallet == -1 :
            return 'You have no wallets'
    @staticmethod
    def get_wallet_by_name(name):
        return Application.db.get_wallet_by_name(name)

    def run(self):
        Menu.app()


if __name__ == '__main__':
    App = Application()
    print(type(Application.db.get_wallet_by_name("Emil's wallet")))
    App.run()
