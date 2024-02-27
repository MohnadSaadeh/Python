
class User :
    def __init__(self ,name , email ): # parameters name emaol_adriss    __init__  Constructer
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposet(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):      
        self.account_balance -= amount
        return self

    def display_user_balance(self ,name):
        print(" User :", name , "\n Balance :" , self.account_balance, "\n" )
        return self
    # HERE IS THE Bouns
    def transfer_money(self, name, amount):
        self.make_withdrawal(amount)
        name.make_deposet(amount)
        return self
    # HERE IS THE Bouns


mohannad = User("mohannad saadeh","m.saadeh.bus@gmail.com")     #object instace from a class
nawar = User("Nawwar","nawar@gmail.com")
aman = User("Aman","aman@gmail.com")

# with chaining method
mohannad.make_deposet(1000).make_deposet(450).make_deposet(50).make_withdrawal(50).display_user_balance("mohannad saadeh") 

nawar.make_deposet(100).make_deposet(50).make_withdrawal(50).display_user_balance("Nawwar")

aman.make_deposet(200).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance("Aman")

#######################################

print("_____________________________")
mohannad.transfer_money(aman,500).display_user_balance("mohannad saadeh")
aman.display_user_balance("Aman")
print("_____________________________")