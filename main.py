from bank_account import BankAccount


def main():

    account1 = BankAccount("Alex", 1000)
    account1.set_balance(-1500)

    print(account1)


main()
