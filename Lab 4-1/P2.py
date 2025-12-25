from BankAccount import BankAccount

accounts = []

john = BankAccount("John", "saving", 500)
tim = BankAccount("Tim", "loan", -1_000_000)
sarah = BankAccount("Sarah", "saving", 0)

accounts.append(john)
accounts.append(tim)
accounts.append(sarah)

john.deposit(3000)
tim.pay_loan((-tim.balance) / 2)
sarah.deposit(50_000_000)

sarah_loan = BankAccount("Sarah", "loan", -100_000_000)
accounts.append(sarah_loan)
for acc in accounts:
    acc.print_customer()
