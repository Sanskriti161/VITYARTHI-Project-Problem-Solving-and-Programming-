## Project Title
Bank Account Simulator

## Overview
A Python-based bank account application that allows users to create accounts, perform various transactions like deposit, withdraw, and manage their account. The application provides a security with features like PIN verification and maintains transaction history for each account.

## Features
- Create new bank accounts along with PIN for security.
- Login to existing accounts with the created account number and PINs.
- Deposit money into your account.
- Withdraw money from your account.
- Check the balance of your account.
- Verify your PIN.
- View your account information.
- View complete transaction history.

## Technologies/Tools Used
- **Language:** Python 3.13.0
- **Libraries:** random (built-in)
- **Concepts:** Data structures (dictionaries, lists), authentication, transaction management

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Sanskriti161/VITYARTHI-Project-Problem-Solving-and-Programming.git
   cd VITYARTHI-Project-Problem-Solving-and-Programming
   ```

2. Ensure Python 3.13.0 is installed:
   ```bash
   python --version
   ```

## How to Run

1. Navigate to the repository folder
2. Run the application:
   ```bash
   python main.py
   ```

3. Follow the prompts:
   - Select option 1 to create a new account (requires initial deposit)
   - Select option 2 to login to an existing account
   - Use the banking menu to perform transactions
   - View account information and transaction history

## Instructions for Testing

**Example Test Case:**

Input:
- Create Account: Account number automatically generated, PIN: 1234, Initial Deposit: ₹5000
- Deposit: ₹1000
- Withdraw: ₹500
- Check Balance: Shows updated balance
- View Transaction History: Shows all transactions

Run unit tests:
```bash
python tests/test_transactions.py
python tests/test_account_manager.py 
```

## Output (Screenshots)

### Screenshot 1: Initial Welcome and Account Creation
![Welcome and Account Creation]<img width="1421" height="531" alt="Initial Welcome and Account Creation" src="https://github.com/user-attachments/assets/e13748a1-5f37-43e9-b03f-9dd53aa7825e" />


### Screenshot 2: Deposit and Withdraw Operations
![Deposit and Withdraw]<img width="1121" height="528" alt="Deposit and Withdraw Operations" src="https://github.com/user-attachments/assets/5f4320b2-adc8-4af3-baec-8a6b16007f06" />

### Screenshot 3: PIN Verification (Incorrect PIN)
![PIN Verification Error]<img width="1018" height="508" alt="PIN Verification (Incorrect PIN)" src="https://github.com/user-attachments/assets/5040fb45-0b62-4d22-b6e6-54d6fedbf5db" />


### Screenshot 4: PIN Verification (Correct PIN)
![PIN Verification Success]<img width="1050" height="506" alt="PIN Verification (Correct PIN)" src="https://github.com/user-attachments/assets/d4644dda-c16b-463e-8e12-37f2d8e855ec" />


### Screenshot 5: View Account Information and Transaction History
![Account Info and Transaction History]<img width="1307" height="637" alt="View Account Information and Transaction History" src="https://github.com/user-attachments/assets/9a2e8167-2295-4b86-96f8-5e6362b1a614" />



### Screenshot 6: Logout and Login to Existing Account
![Logout and Login]<img width="1000" height="556" alt="Logout and Login to Existing Account" src="https://github.com/user-attachments/assets/a7cd1b58-1a5b-4631-b186-9e142df7c378" />

### Screenshot 7: Transaction History and Application Exit
![Transaction History and Exit]<img width="1019" height="664" alt="Transaction History and Application Exi" src="https://github.com/user-attachments/assets/7198ef75-76df-4dce-bc82-8a756f80fc9c" />



## File Structure
```
VITYARTHI-Project-Problem-Solving-and-Programming/
├── main.py
├── account_manager.py
├── transactions.py
├── account_info.py
├── banking_menu.py
├── README.md
├── statement.md
└── tests/
    ├── test_transactions.py
    └── test_account_manager.py
```

## Author
Sanskriti161
