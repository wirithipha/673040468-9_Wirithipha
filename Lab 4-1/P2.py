from BankAccount import BankAccount

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


# Create accounts
john = new_account("John", "saving", 500)
tim = new_account("Tim", "loan", -1_000_000)
sarah = new_account("Sarah", "saving")

# Activities
john.deposit(3000)
tim.pay_loan((-tim.balance) / 2)
sarah.deposit(50_000_000)
new_account("Sarah", "loan", -100_000_000)

# Show all accounts
for acc in accounts:
    acc.print_customer()
