class BankAccount:
    # Class attribute
    branch_name = "KKU Complex"
    branch_number = 1724
    last_loan_number = 0
    last_saving_number = 0

# Private class attributes
#account types
    __type_saving = 1
    __type_loan = 2

# Constructor
    def __init__(self):
        self.name = ""
        self.type = "saving"
        self.balance = 0
        self.account_number = ""

# Instance methods
    def print_customer(self):
        print("----- Customer Record -----")
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Account type: {self.type}")
        print(f"Balance: {self.balance}")
        print("----- End Record -----\n")

    def deposit(self, amount=0):
        self.balance += amount
        return self.balance

    def pay_loan(self, amount=0):
        self.balance += amount
        return self.balance



# ===== Main =====
accounts = []

def new_account(name, acc_type, balance=0):
    acc = BankAccount()
    acc.name = name
    acc.type = acc_type
    acc.balance = balance

    if acc_type == "saving":
        BankAccount.last_saving_number += 1
        t = BankAccount._BankAccount__type_saving
        r = BankAccount.last_saving_number
    else:
        BankAccount.last_loan_number += 1
        t = BankAccount._BankAccount__type_loan
        r = BankAccount.last_loan_number

    acc.account_number = f"{BankAccount.branch_number}-{t}-{r}"
    accounts.append(acc)
    return acc


john = new_account("John", "saving", 500)
tim = new_account("Tim", "loan", -1_000_000)
sarah = new_account("Sarah", "saving")

john.deposit(3000)
tim.pay_loan((-tim.balance) / 2)
sarah.deposit(50_000_000)
new_account("Sarah", "loan", -100000_000)

for a in accounts:
    a.print_customer()
