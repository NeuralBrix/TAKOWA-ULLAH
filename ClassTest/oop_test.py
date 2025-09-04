class bank_account :
    def __init__(self,owner,balance):
        self.balance = balance
        self.owner = owner

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("something else")
    def withdrew(self,amount):
        if self.balance < amount:
            print("balance nai")
        else:
            self.balance -= amount
    def dtails(self):
        print(f"account balance: {self.balance}")
        print(f"account holder: {self.owner}")


x = bank_account("takowa",0)
x.deposit(-7)
x.dtails()


        
        