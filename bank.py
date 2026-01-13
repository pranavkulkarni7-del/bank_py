def bank_transaction(name, acc_no, amount, balance):
    new_balance = balance + amount
    return f"Name: {name}\nAccount: {acc_no}\nAmount: RS {amount}\nOld Balance: RS {balance}\nNew Balance: RS {new_balance}"


# Store data in variables
name1 = "John"
acc_no1 = "123"
amount1 = 500
balance1 = 1000

name2 = "Jane"
acc_no2 = "456"
amount2 = -300
balance2 = 1500

name3 = "Bob"
acc_no3 = "789"
amount3 = 200
balance3 = 800

# Call function with stored variables
print(bank_transaction(name1, acc_no1, amount1, balance1))
print("\n")
print(bank_transaction(name2, acc_no2, amount2, balance2))
print("\n")
print(bank_transaction(name3, acc_no3, amount3, balance3))