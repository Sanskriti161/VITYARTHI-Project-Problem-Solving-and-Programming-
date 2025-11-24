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
![Welcome and Account Creation](https://github.com/Sanskriti161/VITYARTHI-Project-Problem-Solving-and-Programming/raw/main/screenshots/screenshot1.png)

### Screenshot 2: Deposit and Withdraw Operations
![Deposit and Withdraw](https://github.com/Sanskriti161/VITYARTHI-Project-Problem-Solving-and-Programming/raw/main/screenshots/screenshot2.png)

### Screenshot 3: PIN Verification (Incorrect PIN)
![PIN Verification Error](https://github.com/Sanskriti161/VITYARTHI-Project-Problem-Solving-and-Programming/raw/main/screenshots/screenshot3.png)


### Screenshot 4: PIN Verification (Correct PIN)
![PIN Verification Success](https://github.com/Sanskriti161/VITYARTHI-Project-Problem-Solving-and-Programming/raw/main/screenshots/screenshot4.png)


### Screenshot 5: View Account Information and Transaction History
![Account Info and Transaction History](https://github.com/Sanskriti161/VITYARTHI-Project-Problem-Solving-and-Programming/raw/main/screenshots/screenshot5.png)


### Screenshot 6: Logout and Login to Existing Account
![Logout and Login](https://github.com/Sanskriti161/VITYARTHI-Project-Problem-Solving-and-Programming/raw/main/screenshots/screenshot6.png)

### Screenshot 7: Transaction History and Application Exit
![Transaction History and Exit](https://github.com/Sanskriti161/VITYARTHI-Project-Problem-Solving-and-Programming/raw/main/screenshots/screenshot7.png)


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