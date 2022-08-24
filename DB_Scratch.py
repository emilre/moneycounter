import sqlite3
import User, Wallet, Bill


class DBMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DataBase(metaclass=DBMeta):

    def __init__(self, name):
        self.name = name
        '''Сюда должно идти имя базы'''
        # вместо мемори
        self.conn = self.connect(self.name)
        self.cursor = self.conn.cursor()
        self.create_user_table()
        self.create_wallet_table()
        self.create_bills_table()
        self.add_index_user()

    def connect(self, name):
        try:
            return sqlite3.connect(name + '.db')
        except:
            print(sqlite3.Error)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def add_user_db(self, user):
        try:
            print(type(user.id))
            self.cursor.execute('''INSERT INTO users VALUES (? , ?  , ? ,  ? , ?)''',
                                (user.id, user.login, user.name, user.surname, user.password))
            self.commit_db()
            return user
        except:
            return "User already exists!"

    def login_db(self, login, password):
        self.cursor.execute('''SELECT first_name , last_name , login , password, user_id from users WHERE login == ?''',
                            (login,))
        data = self.cursor.fetchone()
        if data == None:
            return 'Such user does not exist'
        if password == data[3]:
            temp_user = User.User(data[0], data[1], data[2], data[3], data[4])
            return temp_user
        return 'Wrong Password'

    def add_wallet_db(self, wallet):
        try:
            print(wallet.id)
            self.cursor.execute('''INSERT INTO wallets VALUES (?,?, ?, ?)''',
                                (str(wallet.id), wallet.wallet_name, wallet.user.login, wallet.balance))
            self.commit_db()
            print('Success')
        except:
            return 'Error'

    def get_user_by_wallet(self, name):

        self.cursor.execute(
            '''SELECT first_name , last_name , login , password, user_id FROM users CROSS JOIN wallets where login = ?''',
            (name,))
        data = self.cursor.fetchone()
        if data is None:
            return 'Error'
        return User.User(data[0], data[1], data[2], data[3], data[4])
        # temp = User.User(data[0][2], data[0][3], data[0][1], data[0][4])

    def get_wallet_by_name(self, name):
        self.cursor.execute('''SELECT * FROM wallets WHERE wallet_name = ?''', (name,))
        data = self.cursor.fetchone()

        if data is None:
            return 'such wallet does not exist'
        else:

            return Wallet.Wallet(self.get_user_by_wallet(data[2]), data[1], data[3], data[0])
        # return User(data[0],

    #         Application.db.cursor.execute('''SELECT * FROM users cross join wallets''') croos joim собрать изера и кошелек
    def show_wallets_of_user(self, user):
        self.cursor.execute('''SELECT * from wallets WHERE wallet_owner == ?''', (user.login,))
        data = self.cursor.fetchall()
        if len(data):
            wallet_list = [elem for elem in data]
            print(wallet_list)
            return data
        else:
            return -1

    def delete_wallet(self, wallet_name):
        try:
            self.cursor.execute('''DELETE from wallets WHERE wallet_name = ?''', (wallet_name,))
            self.commit_db()
            print('Success')
        except:
            return 'Such wallet does not exist '

    def add_bill_db(self, bill):
        # каждый раз когда вызывается этот метод , должен апдейтаться баланс по кошельку
        current_bal = bill.wallet.balance + bill.amount
        self.cursor.execute('''UPDATE wallets SET balance = ? WHERE wallet_name = ?''',(current_bal,bill.wallet.wallet_name))
        self.cursor.execute('''INSERT INTO bills VALUES (? , ?, ? , ?, ? , ?,?) ''',
                            (bill.id, bill.amount, bill.date, bill.category,
                             bill.name, None, bill.wallet.wallet_name))
        self.commit_db()

    def show_user_table(self):
        self.cursor.execute('''SELECT * FROM users''')
        data = self.cursor.fetchall()
        print(data)

    '''CREATE UNIQUE INDEX user_id_index 
        ON users(user_id)'''

    def add_index_user(self):
        try:
            self.cursor.execute('''CREATE INDEX user_id_index ON users(user_id)''')
        except:
            return "user_id_index ON users(user_id) is indexed"

        self.commit_db()

    def add_index_wallet(self):
        self.cursor.execute('''CREATE UNIQUE INDEX wallet_id_index 
         ON wallets(wallet_id)''')
        self.commit_db()

    def add_index_bill(self):
        self.cursor.execute('''CREATE UNIQUE INDEX bill_id_index 
         ON bills(bill_id)''')
        self.commit_db()

    def user_exists(self, login):
        self.cursor.execute('''SELECT login FROM USERS WHERE login = {}'''.format(login))
        if self.cursor.fetchone():
            return True

    def create_user_table(self):
        __create_user_table_q = """CREATE TABLE IF NOT EXISTS users(
                            user_id TEXT PRIMARY KEY,
                            login TEXT UNIQUE NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            password TEXT NOT NULL
                            )"""
        self.cursor.execute(__create_user_table_q)
        self.commit_db()

    def create_wallet_table(self):
        create_wallets_q = """CREATE TABLE IF NOT EXISTS  wallets (
                wallet_id TEXT PRIMARY KEY ,
                wallet_name TEXT UNIQUE NOT NULL, 
                wallet_owner TEXT NOT NULL ,
                balance FLOAT DEFAULT 0.0 NOT NULL  ,
                FOREIGN KEY(wallet_owner) REFERENCES users(login)
         )"""
        self.cursor.execute(create_wallets_q)
        self.commit_db()

    def create_bills_table(self):

        create_bills_q = """ CREATE TABLE IF NOT EXISTS bills (
                bill_id TEXT NOT NULL UNIQUE,
                amount FLOAT NOT NULL,
                date TIMESTAMP ,
                category TEXT,
                bill_name TEXT, 
                cash_back_flag INT,
                wallet TEXT ,
                FOREIGN KEY(wallet) REFERENCES wallets(wallet_name)
        )
        """
        self.cursor.execute(create_bills_q)

    def commit_db(self):
        self.conn.commit()

    def show_all_tables(self):
        self.conn.execute('''SELECT name FROM sqlite_schema
                                WHERE type='table'
                                ORDER BY name;''')
        data = self.cursor.fetchall()
        print(data)
# # Create a Table
# c.execute(create_user_table_q)
# c.execute(create_wallets_q)
# #
#
# c.execute("INSERT INTO users VALUES ('1','login', 'Emil', 'Rasulzade', 'password1')")
# c.execute("INSERT INTO users VALUES ('2','login2', 'Ayla', 'Rasulzade', 'password2')")
# c.execute("INSERT INTO users VALUES ('3','login3', 'Emin', 'Rasulzade', 'password3')")
# c.execute("INSERT INTO wallets VALUES ('1', 'login', '0')")
# c.execute("INSERT INTO wallets VALUES ('2','login')")
# c.execute("SELECT * FROM users")
# users = c.fetchall()
# for elem in users:
#     print(elem)
# c.execute("SELECT * FROM wallets")
# print()
# print()
# users = c.fetchall()
# for elem in users:
#     print(elem)
# # Commit
# conn.commit()
# # close conn
# conn.close()
