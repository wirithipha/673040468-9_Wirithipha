class BankAccount:
# Class attribute
    branch_name = "KKU Complex"
    branch_number = 1724
    last_loan_number = 0
    last_saving_number = 0

# Private class atttributes
# accoount types
    __type_saving = 1
    __type_loan = 2

# Constructor
    def __init__(self, name, acc_type="saving", balance=0):
        self.name = name
        self.balance = balance

        if acc_type == "saving":
            self.type = BankAccount.__type_saving
            BankAccount.last_saving_number += 1
            self.account_number = (
                str(BankAccount.branch_number)
                + "1"
                + str(BankAccount.last_saving_number)
            )
        else:
            self.type = BankAccount.__type_loan
            BankAccount.last_loan_number += 1
            self.account_number = (
                str(BankAccount.branch_number)
                + "2"
                + str(BankAccount.last_loan_number)
            )

# Instance methods
    def print_customer(self):
        print(self.name, self.account_number, self.balance)

    def deposit(self, amount=0):
        if self.type == BankAccount.__type_saving:
            self.balance += amount
        return self.balance

    def withdraw(self, amount=0):
        if self.type == BankAccount.__type_saving and amount <= self.balance:
            self.balance -= amount
        return self.balance

    def pay_loan(self, amount=0):
        if self.type == BankAccount.__type_loan:
            self.balance += amount
        return self.balance

    def get_loan(self, amount=0):
        if self.type == BankAccount.__type_loan and self.balance - amount >= -50000:
            self.balance -= amount
        return self.balance
