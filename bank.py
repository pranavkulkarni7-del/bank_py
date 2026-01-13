# Simple Transaction System - Normal Flow

print("=== Transaction System ===\n")

# Initial balance
balance = 1000
print(f"Starting Balance: RS {balance}")

# Transaction 1: Deposit
deposit_amount = 500
balance = balance + deposit_amount
print(f"\nDeposit: +RS {deposit_amount}")
print(f"Balance: RS {balance}")

# Transaction 2: Withdrawal
withdraw_amount = 200
balance = balance - withdraw_amount
print(f"\nWithdrawal: -RS {withdraw_amount}")
print(f"Balance: RS {balance}")

# Transaction 3: Deposit
deposit_amount = 300
balance = balance + deposit_amount
print(f"\nDeposit: +RS {deposit_amount}")
print(f"Balance: RS {balance}")

# Transaction 4: Withdrawal
withdraw_amount = 150
balance = balance - withdraw_amount
print(f"\nWithdrawal: -RS {withdraw_amount}")
print(f"Balance: RS {balance}")

# Final summary
print(f"\n=== Summary ===")
print(f"Final Balance: RS {balance}")