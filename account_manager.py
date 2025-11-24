import random

all_accounts = {}

def create_account():
    print("Create New Account:")

    account_num = random.randint(100000000000, 999999999999)
    acc_num = str(account_num)
    print(f"Your new account number is: {acc_num} (write it down!)")

    while True:
        pin = input("Set your 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            print("PIN set successfully.")
            break
        else:
            print("Oh no. Error! PIN must be 4 digits.")

    while True:
        deposit = input("Enter your initial deposit amount: ")
        try:
            initial_deposit = float(deposit)
            if initial_deposit > 0:
                print(f"Initial deposit of ₹{initial_deposit:.2f} successful.")
                break
            else:
                print("Amount has to be positive.")
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")

    new_acc = {
        'account_number': acc_num,
        'pin': pin,
        'balance': initial_deposit,
        'transaction_history': []
    }

    global all_accounts
    all_accounts[acc_num] = new_acc

    print(f"\nAccount Successfully Created! 🥳 \nWelcome New User \nAccount Number: {new_acc['account_number']}\nInitial Balance: ₹{new_acc['balance']:.2f}\nPIN: {'*' * len(new_acc['pin'])}")
    return new_acc

def login_to_account(all_accounts):
    print("\nAccount Login")
    acc_num_input = input("Enter your account number: ")
    pin_input = input("Enter your 4-digit PIN: ")

    if acc_num_input in all_accounts:
        account = all_accounts[acc_num_input]
        if account['pin'] == pin_input:
            print("Login successful!")
            return account
        else:
            print("Oh no. Error! Provided PIN is incorrect. Please try again.")
    else:
        print("Oh no. Error! Account number not found. Please try again.")
    return None