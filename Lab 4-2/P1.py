from BankAccount import BankAccount

if __name__ == "__main__":
    # saving account
    a = BankAccount("Nene", "saving", 1000)
    a.deposit(500)
    a.withdraw(200)
    a.print_customer()

    # loan account
    b = BankAccount("Nene", "loan", -10000)
    b.get_loan(5000)
    b.pay_loan(3000)
    b.print_customer()
