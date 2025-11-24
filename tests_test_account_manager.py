import sys
sys.path.insert(0, '..')

from account_info import verify_pin, view_account_info

# Test account verification
test_account = {
    'account_number': '123456789',
    'pin': '1234',
    'balance': 5000,
    'transaction_history': ['Deposit: +₹1000']
}

print("Testing Account Manager Module:")
print("=" * 50)

print("\nTest 1: PIN Verification (Correct)")
result = verify_pin(test_account, '1234')
assert result == True, "PIN verification failed"
print("✓ PIN verified successfully")

print("\nTest 2: PIN Verification (Incorrect)")
result = verify_pin(test_account, '0000')
assert result == False, "PIN verification should fail"
print("✓ Incorrect PIN rejected")

print("\nTest 3: View Account Info")
view_account_info(test_account)

print("\n" + "=" * 50)
print("✓ All account manager tests passed")