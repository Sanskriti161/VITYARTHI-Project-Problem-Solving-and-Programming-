def verify_pin(account_details, user_pin):
    return account_details['pin'] == user_pin

def view_account_info(account_details):
    print("\nHere is your Account Information: ")
    print(f"Account Number: {account_details['account_number']}")
    print(f"Current Balance: ₹{account_details['balance']:.2f}")
    print(f"PIN: {'*' * len(account_details['pin'])}")

def view_transaction_history(account_details):
    print("\nHere is your Transaction History: ")
    if account_details['transaction_history']:
        for transaction in account_details['transaction_history']:
            print(transaction)
    else:
        print("No transactions yet.")