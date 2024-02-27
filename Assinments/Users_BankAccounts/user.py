
class BankAccount:
    def __init__(self, int_rate , balance):
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

    def display_amount_info(self ,name):
        print("Balance: for ", name ," =  ",self.balance ,"NIS")

    def yield_interests(self):
        interests = 0.00
        if self.balance > 0 :
            interest = self.balance * self.int_rate
        print("\nyield interest" , interests)
        return self



shekel =    BankAccount(0.02,0)
dolar =     BankAccount(0.03 ,0)
dinar =     BankAccount(0.02,0)




class User :
    def __init__(self ,name , email , acc_kind): # parameters name emaol_adriss    __init__  Constructer
        self.name = name
        self.email = email
        self.acc_kind = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposet(self ,amount,acc_kind):
        self.acc_kind.deposet(amount)                     # in this methods, we can now access the BankAccount class through our self.account attribute, 
        return self

    def make_withdrawal(self, amount,acc_kind):      
        self.acc_kind.withdraw(amount)
        return self

    def display_user_balance(self ,name):
        self.acc_kind.display_amount_info(name)
        # print(" User :", name , "\n Balance :" , self.shekel.balance , "\n" )

        return self
    # HERE IS THE Bouns
    def transfer_money(self, name, amount,acc_kind):
        self.make_withdrawal(amount,acc_kind)
        name.make_deposet(amount,acc_kind)
        return self
    # HERE IS THE Bouns


mohannad =  User("mohnad","m.saadeh.bus@gmail.com" ,shekel)     #object instace from a class
mohannad =  User("mohnad","m.saadeh.bus@gmail.com" ,dolar) 
nawar =     User("Nawwar","nawar@gmail.com",shekel)
nawar =     User("Nawwar","nawar@gmail.com",dolar)
aman =      User("Amaaan","aman@gmail.com"  , shekel)
aman =      User("Amaaan","aman@gmail.com", dolar)



# with chaining method
mohannad.make_deposet(1000,shekel).make_deposet(450,shekel).make_deposet(50,shekel).make_withdrawal(50,shekel).display_user_balance("mohnad") 

nawar.make_deposet(100,dolar).make_deposet(50,dolar).make_withdrawal(50,dolar).display_user_balance("Nawwar")

aman.make_deposet(200,dolar).make_withdrawal(50,dolar).make_withdrawal(100,dolar).make_withdrawal(50,dolar).display_user_balance("Amaaan")

#######################################

print("_____________________________")
mohannad.transfer_money(aman,500,dolar).display_user_balance("mohnad")
aman.display_user_balance("Amaaan")
print("_____________________________")



