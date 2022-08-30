import tkinter as tk
import tkinter.ttk as ttk

usr= None
wallet= None
bill = None
win = tk.Tk()
win.geometry('400x400')
# build ui
# login frame
login_frame_log = ttk.Frame(win)
login_frame_log.configure(height=400, width=400)
login_label_log = ttk.Label(login_frame_log)
login_label_log.configure(text="Login : \t")
login_label_log.place(relx=0.0, x=100, y=150)
password_lbl_log = ttk.Label(login_frame_log)
password_lbl_log.configure(text="Password : \t")
password_lbl_log.place(relx=0.0, x=100, y=200)
password_entry_log = ttk.Entry(login_frame_log)
password_entry_log.place(x=200, y=200)
login_entry_log = ttk.Entry(login_frame_log)
login_entry_log.place(x=200, y=150)
greet_label_log = tk.Label(login_frame_log)
greet_label_log.configure(
    activebackground="Blue", background="#20c2df", text="Hello to MoneyCounter"
)
greet_label_log.place(x=130, y=50)
register_btn_log = tk.Button(login_frame_log, command=lambda: to_register())
register_btn_log.configure(text="Register ")
register_btn_log.place(width=80, x=100, y=240)
info_label_log = tk.Label(login_frame_log)
info_label_log.configure(
    background="#94a9f3", text="Input your login and password!"
)
info_label_log.place(x=110, y=100)
login_btn_log = tk.Button(login_frame_log)
login_btn_log.configure(text="Login",command=lambda : to_in_app())
login_btn_log.place(width=80, x=220, y=240)
login_lbl_log = tk.Message(login_frame_log)
login_lbl_log.configure(background="#fbea8c", text="Login Error!")
login_lbl_log.place(x=325, y=148)
password_message_log = tk.Message(login_frame_log)
password_message_log.configure(background="#fbea8c", text="Wrong Password!")
password_message_log.place(width=80, x=325, y=190)
login_frame_log.place(x=0, y=0)

# register frame


reg_frame = ttk.Frame(win)
reg_frame.configure(height=400, width=400)

name_label_reg = ttk.Label(reg_frame)
name_label_reg.configure(text="Name : \t")
name_label_reg.place(x=100, y=150)

surname_label_reg = ttk.Label(reg_frame)
surname_label_reg.configure(text="Surname : \t")
surname_label_reg.place(relx=0.0, x=100, y=200)
surname_entry_reg = ttk.Entry(reg_frame)
surname_entry_reg.place(x=200, y=200)
login_entry_reg = ttk.Entry(reg_frame)
login_entry_reg.place(x=200, y=150)
greet_label_reg = tk.Label(reg_frame)
greet_label_reg.configure(
    activebackground="Blue", background="#20c2df", text="Hello to MoneyCounter"
)
greet_label_reg.place(x=130, y=50)
abort_button_reg = tk.Button(reg_frame)
abort_button_reg.configure(text="Abort", command=lambda: abort())
abort_button_reg.place(width=80, x=100, y=240)
info_label_reg = tk.Label(reg_frame)
info_label_reg.configure(
    background="#94a9f3", text="Input your name and surname!"
)
info_label_reg.place(x=110, y=100)
next_button_reg = tk.Button(reg_frame)
next_button_reg.configure(text="Next->", command=lambda: to_register_2())
next_button_reg.place(width=80, x=220, y=240)
name_msg_reg = tk.Message(reg_frame)
name_msg_reg.configure(background="#fbea8c", text="Name Error!")
name_msg_reg.place(x=325, y=148)
surname_msg_reg = tk.Message(reg_frame)
surname_msg_reg.configure(background="#fbea8c", text="Surname Error!")
surname_msg_reg.place(width=80, x=325, y=190)

# register 2 frame


reg2_frame = ttk.Frame()
reg2_frame.configure(height=400, width=400)
login_label_reg2 = ttk.Label(reg2_frame)
login_label_reg2.configure(text="Login : \t")
login_label_reg2.place(relx=0.0, x=100, y=150)
password_label_reg2 = ttk.Label(reg2_frame)
password_label_reg2.configure(text="Password : \t")
password_label_reg2.place(relx=0.0, x=100, y=200)
password_entry_reg2 = ttk.Entry(reg2_frame)
password_entry_reg2.place(x=200, y=200)
login_entry_reg2 = ttk.Entry(reg2_frame)
login_entry_reg2.place(x=200, y=150)
greet_label_reg2 = tk.Label(reg2_frame)
greet_label_reg2.configure(
    activebackground="Blue", background="#20c2df", text="Hello to MoneyCounter"
)
greet_label_reg2.place(x=130, y=50)
abort_button2_reg2 = tk.Button(reg2_frame)
abort_button2_reg2.configure(text="Abort", command=lambda: abort())
abort_button2_reg2.place(width=80, x=100, y=240)
info_label_reg2 = tk.Label(reg2_frame)
info_label_reg2.configure(
    background="#94a9f3", text="Input your login and password!"
)
info_label_reg2.place(x=110, y=100)
Finish_reg2 = tk.Button(reg2_frame,command = lambda: abort())
Finish_reg2.configure(text="Finish")
Finish_reg2.place(width=80, x=220, y=240)
login_msg_reg2 = tk.Message(reg2_frame)
login_msg_reg2.configure(background="#fbea8c", text="Login Error!")
login_msg_reg2.place(x=325, y=148)
password_msg_reg2 = tk.Message(reg2_frame)
password_msg_reg2.configure(background="#fbea8c", text="Password Error")
password_msg_reg2.place(width=80, x=320, y=190)

# in_app screen


in_app = ttk.Frame()
in_app.configure(height=400, width=400)
wallet_in_app_choice = tk.Button(in_app)
wallet_in_app_choice.configure(text="Choose a Wallet ",command=lambda: choose_wallet_in_app())
wallet_in_app_choice.place(anchor="nw", width=150, x=125, y=75)
wallets_list_in_app = tk.Listbox(in_app)
wallets_list_in_app.place(width=150, x=125, y=95)
create_wallet_button_in_app = tk.Button(in_app)
create_wallet_button_in_app.configure(text="Create a Wallet",command = lambda : create_wallet_in_app())
create_wallet_button_in_app.place(width=150, x=125, y=260)
wallet_name_entryin_app = tk.Entry(in_app)
wallet_name_entryin_app.place(height=30, width=150, x=125, y=287)
greet_label_in_app = tk.Label(in_app)
greet_label_in_app.configure(
    background="#94a9f3", text="Greetings username!"
)
greet_label_in_app.place(width=200, x=100, y=25)
delete_wallet_button = tk.Button(in_app)
delete_wallet_button.configure(
    cursor="arrow", text="Delete a choosen wallet" ,command = lambda : delete_wallet_in_app()
)
delete_wallet_button.place(anchor="nw", height=30, width=150, x=125, y=340)

# in wallet screen


in_wallet = ttk.Frame()
in_wallet.configure(height=400, width=400)
bills_list_in_wallet = tk.Listbox(in_wallet)
bills_list_in_wallet.place(width=150, x=125, y=95)
create_bill_button_in_wallet = tk.Button(in_wallet)
create_bill_button_in_wallet.configure(text="Create a Bill")
create_bill_button_in_wallet.place(width=150, x=125, y=260)
wallet_name_entry_in_wallet = tk.Entry(self.in_wallet)
wallet_name_entry_in_wallet.place(height=30, width=150, x=125, y=287)
greet_label_in_wallet = tk.Label(in_wallet)
greet_label_in_wallet.configure(
    background="#94a9f3", justify="left", text="Wallet : wallet_name"
)
greet_label_in_wallet.place(width=200, x=100, y=25)
delete_bill_button = tk.Button(in_wallet)
delete_bill_button.configure(cursor="arrow", text="Delete a choosen Bill")
delete_bill_button.place(anchor="nw", height=30, width=150, x=125, y=340)
in_wallet.place(x=0, y=0)


def delete_wallet_in_app():
    pass
def to_register():
    reg_frame.place(x=0, y=0)
def choose_wallet_in_app():
    pass
def to_in_app():
    in_app.place(x=0,y=0)
def abort():
    reg_frame.place_forget()
    reg2_frame.place_forget()
    login_frame_log.place(x=0, y=0)

def create_wallet_in_app():
    pass
def to_register_2():
    reg_frame.place_forget()
    reg2_frame.place(x=0, y=0)


# def get_login():
#     login = login_entry_log.get()
#     password = password_entry_log.get()
#     user = App.Application.login(login, password)
#     if type(user) is str:
#         return user
#     global usr
#     usr = user
#     return usr


win.mainloop()
