import App
import User
from Wallet import Wallet
import Bill


#


def login():
    while True:
        login_flag = False
        print_login()
        temp_user_input = input()
        if user_input_validation(temp_user_input, 'login'):
            user_input = int(temp_user_input)
            if user_input == 1:
                user = App.Application.login(input("Login : "), input("Password : "))
                if not isinstance(user, User.User):
                    print(user)
                    continue
                else:
                    login_flag = True
                    break
            if user_input == 2:
                user = App.Application.register(input("Name : "), input("Surname : "), input("Login : "),
                                                input("Password  : "))
                if type(user) is str:
                    print(user)

            if user_input == 3:
                print("Good luck!")
                return 0
        else:
            print("Invalid input , try again !")
    if login_flag:
        in_app(user)


def in_app(user):
    in_wallet_flag = False
    to_login_flag = False
    while True:
        wallet = None
        print_in_app()
        temp_user_input = input()
        if user_input_validation(temp_user_input, 'in_app'):
            user_input = int(temp_user_input)
            if user_input == 1:
                if user.has_wallet():
                    wallet_name = input("Enter a Wallet Name You Want to Choose : ")

                    wallet = App.Application.get_wallet_by_name(wallet_name)
                    if type(wallet) is str or None:
                        print(wallet)
                        continue
                    in_wallet_flag = True
                    break
                print("You have no Wallets")

            if user_input == 2:
                wallet = user.create_wallet(input('Wallet name : '))
                if type(wallet) == str:
                    print(wallet)

            if user_input == 3:
                wallet_name = input("Enter a Wallet Name You Want to Delete : ")
                user.delete_wallet(wallet_name)

            if user_input == 4:
                user.print_all_wallets()
            if user_input == 5:
                to_login_flag = True
                break
        else:
            print("Invalid input , try again !")
    if in_wallet_flag:
        in_wallet(wallet)
    if to_login_flag:
        login()


# Сделать валидацию всех инпутов !!!
def in_wallet(wallet):
    to_in_app_flag = False
    while True:
        print_in_wallet()
        # SDELAT' STATISTIKU
        temp_user_input = input()
        if user_input_validation(temp_user_input, 'in_wallet'):
            user_input = int(temp_user_input)
            if user_input == 1:
                print("[1]Spending")
                print("[2]Income")
                temp_user_input = input()
                if user_input_validation(temp_user_input, 'in_Bill'):
                    # Доделать эту часть
                    user_input_in = int(temp_user_input)
                    if user_input_in == 1:
                        bill_info = input_bill_info()
                        if type(bill_info) is not str:
                            wallet.add_bill(Bill.Bill(bill_info[0]*-1, bill_info[1], bill_info[2], wallet))

                    if user_input_in == 2:
                        bill_info = input_bill_info()
                        if type(bill_info) is not str:
                            wallet.add_bill(Bill.Bill(bill_info[0] , bill_info[1], bill_info[2], wallet))
            if user_input == 2:
                print("Wallet : " + wallet.wallet_name + " has ", wallet.balance, " currency ")
                continue
            if user_input == 3:
                cash_back_category = input('Input a category to set a cashback on')
                wallet.set_cashback_category(cash_back_category)
                continue
            if user_input == 5:
                pass
            if user_input == 6:
                to_in_app_flag = True
                break
    if to_in_app_flag:
        in_app(wallet.get_user_by_wallet)


def print_in_wallet():
    print('[1] Add a Bill')
    print('[2] Check balance')
    print('[3] Show all transactions')
    print('[4] Delete a bill')
    print('<------------>')
    print('[5] See Statistics')
    print('[6] Go back to Wallet management ')


def print_login():
    print('[1] Sign IN')
    print('[2] Sign UP')
    print('<------------>')
    print('[3] EXIT')


def print_in_app():
    print('[1] Choose a Wallet')
    print('[2] Create Wallet')
    print('[3] Delete Wallet')
    print('[4] Show Wallets')
    print('<------------>')
    print('[5] Log out')


def input_bill_info():
    try :
        amount = float(input("Input the amount of the Bill : "))
    except TypeError:
        return 'Type Error , numeric values in amount!'

    category = input("Input the category of the Bill : ")
    if category.isalpha() :
        name = input("Input the name of the Bill : ")
        if name.isalpha():
            return amount, category, name
        else: return 'Name should not contain numbers'
    else: return 'Category should not contain numbers'



def user_input_validation(input, state):
    if state == 'login':
        return input.isnumeric() and int(input) in range(1, 4)
    if state == 'in_app':
        return input.isnumeric() and int(input) in range(1, 6)
    if state == 'in_wallet':
        return input.isnumeric() and int(input) in range(1, 7)
    if state == 'in_Bill':
        return input.isnumeric() and int(input) in range(1, 3)


def app():
    login()
