from transactions import deposit, withdraw, check_balance
from account_info import verify_pin, view_account_info, view_transaction_history

def banking_menu_loop(account_details):
    print(f"\nWelcome, User 😊: {account_details['account_number']} ---")
    while True:
        print("\nBanking Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Verify PIN")
        print("5. View Account Info")
        print("6. View Transaction History")
        print("7. Logout")

        choice = input("Enter your choice (1 to 7): ")

        if choice == '1':
            while True:
                amount_str = input("Enter deposit amount: ")
                try:
                    amount = float(amount_str)
                    deposit(account_details, amount)
                    break
                except ValueError:
                    print("Oh no. Errror!. Please enter a numerical value.")
        elif choice == '2':
            while True:
                amount_str = input("Enter withdrawal amount: ")
                try:
                    amount = float(amount_str)
                    withdraw(account_details, amount)
                    break
                except ValueError:
                    print("Oh no. Error! Please enter a numerical value.")
        elif choice == '3':
            check_balance(account_details)
        elif choice == '4':
            user_pin_input = input("Enter your PIN to verify: ")
            if verify_pin(account_details, user_pin_input):
                print("PIN is correct.")
            else:
                print("Oh no. The provided PIN is incorrect. Try again.")
        elif choice == '5':
            view_account_info(account_details)
        elif choice == '6':
            view_transaction_history(account_details)
        elif choice == '7':
            print("Logging out of current account. Hopefully I was helpful 😊.")
            break 
        else:
            print("Oh no. Error! Please enter a number between 1 and 7.")