from account_manager import create_account, login_to_account, all_accounts
from banking_menu import banking_menu_loop

print("\nWelcome to my Banking Application")

while True:
    print("\nSelection Menu")
    print("1. Create New Account")
    print("2. Login to Existing Account")
    print("3. Exit")

    choice = input("Enter your choice (1 to 3): ")

    active_account = None

    if choice == '1':
        active_account = create_account()
        if active_account:
            print("Account created and set as active.")
            banking_menu_loop(active_account) 
    
    elif choice == '2':
        active_account = login_to_account(all_accounts)
        if active_account:
            print("Login successful. Account set as active.")
            banking_menu_loop(active_account)
       
    elif choice == '3':
        print("Thank you for using my Banking Application 😊😊.")
        break
    else:
        print("Oh no. Error! Please enter 1, 2, or 3.")