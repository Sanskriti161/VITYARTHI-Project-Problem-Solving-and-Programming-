import sys
sys.path.insert(0, '..')

from transactions import deposit, withdraw, check_balance

# Test deposit
test_account = {
    'account_number': '123456789',
    'pin': '1234',
    'balance': 1000,
    'transaction_history': []
}

print("Testing Transactions Module:")
print("=" * 50)

print("\nTest 1: Deposit")
deposit(test_account, 500)
assert test_account['balance'] == 1500, "Deposit failed"

print("\nTest 2: Withdraw")
withdraw(test_account, 300)
assert test_account['balance'] == 1200, "Withdraw failed"

print("\nTest 3: Check Balance")
check_balance(test_account)

print("\n" + "=" * 50)
print("✓ All transaction tests passed")