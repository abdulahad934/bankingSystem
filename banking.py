import datetime
class Bank:
    bank_name = "smart National Bank"
    customers = []
    def __init__(self):
        print(f"Welcome to {self.bank_name}\n")
    def register_customer(self, customer):
        Bank.customers.append(customer)
    
    def find_customer(self, username, password):
        for c in Bank.customers:
            if c.username == username and c.password == password:
                return c
            return None
     
    def show_all_customers(self):
         print("All registered customers:")
         
         for c in Bank.customers:
            print(f"Name: {c.name}, | Username: {c.username}, | Balance: {c.balance}")



class Customer:
    def __init__(self, name, username, password, acount_type = "savings"):
        self.name = name
        self.username = username
        self.password = password
        self.acount_type = acount_type
        self.balance = 0
        self.history = []
        self.created_at = datetime.datetime.now()
        self.first_time_bonus_given = False
    
    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: {amount} at {datetime.datetime.now()}")
            print(f"Deposit successfully new balance is {self.balance}")
            if not self.first_time_bonus_given:
                self.balance += 100
                self.history.append(f"First time bonus added: 100")
                print("First time customer bonus : 100")
                self.first_time_bonus_given = True
        else:
            print("Invalid Deposit Amount. ")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"withdrawn: {amount} at {datetime.datetime.now()}")
            print(f"Withdrawn successfully new balance is {self.balance}")
        else:
            print("Invalid withdraw Amount ")
            
    
    def check_balance(self):
        if self.username and self.password:
            print(f"Current balance is {self.balance}")
        else:
            print("Please login to check your balance.")
    
    def transfer(self, recover, amount):
        if o < amount <= self.balance:
            self.balance -= amount
            recover.balance += amount
            self.history.append(f"Transferred: {amount} to {recover.username} at {datetime.datetime.now()}")
            recover.history.append(f"Recovered: {amount} from {self.username} at {datetime.datetime.now()}")
            print(f"Transfer successful. New balance is {self.balance}")
        else:
            print("Invalid transfer amount or insufficient balance.")
    def show_history(self):
        print(f"Transaction history of {self.name}")
        for h in self.history:
            print(h)
            