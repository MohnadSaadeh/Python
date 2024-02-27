class BankAccount:
    def __init__( self,int_rate  , balance  ):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposet(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee and deduct $5")
        return self

    def display_amount_info(self):
        print("Balance: $" ,self.balance)

    def yield_interests(self):
        interests = 0.00
        if self.balance > 0 :
            interest = self.balance * self.int_rate
        print("\nyield interest" , interests)
        return self

shekel = BankAccount(0.01 , 0)
dolar = BankAccount()

# 7
shekel.deposet(100).deposet(50).deposet(50).withdraw(50).display_amount_info()

# 8
dolar.deposet(100).deposet(100).withdraw(50).withdraw(50).withdraw(100).withdraw(50).yield_interests().display_amount_info()


