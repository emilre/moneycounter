import uuid
from datetime import datetime

from App import Wallet, DataBase, Application


# index vozvrazaet perviy popavvwiysa index. Ima u ojectov povtoratsa ne dolno .
# Sdelat' menu s rabochem funtionalom

# unique username


class User:

    def __init__(self, name: str, surname: str, login: str, password: str, id=uuid.uuid4()):
        self.id = str(id)
        self.Wallet_list = []
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password

    def create_wallet(self, wallet_name):
        temp_wallet = Wallet.Wallet(self, wallet_name)
        Application.add_wallet(temp_wallet)

    def delete_wallet(self, wallet_name):
        Application.db.delete_wallet(wallet_name)

    # Не знаю правильно ли я написал этот метод . ( Правильно)
    def get_wallet_by_name(self, name: str):
        Application.get_wallet_by_name(name)

    def has_wallet(self):
        if Application.db.show_wallets_of_user(self) == -1:
            return False
        return True

    def get_wallet_index_by_name(self, name: str):
        index = 0
        for elem in self.Wallet_list:
            if elem.wallet_name == name:
                return self.Wallet_list.index(elem)  ## furutu

    def get_wallet_index_by_id(self, id: str):
        for elem in self.Wallet_list:
            if id == id:
                print(self.Wallet_list.index(elem))
        pass

    def print_all_wallets(self):
        return Application.show_all_wallet_of_user(self)

    def __str__(self):
        return 'My name is ' + self.name
#
# A = User('Emil', 'Rasulzade', 'emilka', 'parol')
# A.create_wallet('Kashel')
# A.get_wallet_index_by_name('Kashel')
#
#


###################################### mnu
