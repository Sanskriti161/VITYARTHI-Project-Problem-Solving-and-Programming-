def deposit(account_details, amount):
    if amount > 0:
        account_details['balance'] += amount
        account_details['transaction_history'].append(f"Deposit: +₹{amount:.2f} | New Balance: ₹{account_details['balance']:.2f}")
        print(f"Deposit of ₹{amount:.2f} successful. New balance: ₹{account_details['balance']:.2f}")
    else:
        print("Deposit amount must be positive.")

def withdraw(account_details, amount):
    if amount > 0:
        if account_details['balance'] >= amount:
            account_details['balance'] -= amount
            account_details['transaction_history'].append(f"Withdrawal: -₹{amount:.2f} | New Balance: ₹{account_details['balance']:.2f}")
            print(f"Withdrawal of ₹{amount:.2f} successful. New balance: ₹{account_details['balance']:.2f}")
        else:
            print("Oh no, Not enough balance.")
    else:
        print("Withdrawal amount must be positive.")

def check_balance(account_details):
    print(f"Current balance: ₹{account_details['balance']:.2f}")