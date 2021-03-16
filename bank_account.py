class BANKACCOUNT:
    def __init__(self, int_rate=0, balance=0):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("ERROR: Insufficent funds!")
        return self

    def display_account_info(self):
        print(
            f"Current account balance is: ${self.balance}.")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += round(self.balance*self.interest)
        else:
            print("No positive balance to calculate intrest toward.")
        return self


chime = BANKACCOUNT(0.005, 1400)
ibc = BANKACCOUNT(0.00067, 500)

chime.deposit(1200).deposit(80).deposit(20).withdraw(
    700).yield_interest().display_account_info()

ibc.deposit(1400).deposit(200).withdraw(200).withdraw(900).withdraw(
    70).withdraw(160).yield_interest().display_account_info()
