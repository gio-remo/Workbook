class Category():
    
    def __init__(self, cname):
        self.name = cname
        self.balance = 0
        self.deposits = 0
        self.withdraws = 0
        self.ledger = []

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.deposits += amount
        self.balance += amount
        self.ledger.append({"amount": amount, "description": str(description)}) # Each item in the list "ledger" is a dictionary of two properties

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraws += amount
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": str(description)})
            return True

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, dcategory):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraws += amount
            self.balance -= amount
            dcategory.deposits += amount
            dcategory.balance += amount
            self.ledger.append({"amount": -amount, "description": "Transfer to " + dcategory.name})
            dcategory.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
            return True
    
    # Stampa Oggetto
    def __str__(self):
        print = self.name.center(30,"*") + "\n" # WOW!! str.CENTER(length)
        for i in self.ledger:
            if len(i["description"]) > 23:
                print += "{:23}".format(i["description"][:23]) # Cut string if longer
            else:
                print += "{:23}".format(i["description"])
            print += "{:7.2f}".format(float(i["amount"])) + "\n" # Format: 7 char width, 2 float decimals
        print += "Total: " + str("{:.2f}".format(float(self.balance)))
        return print

def create_spend_chart(categories):
    
    s = "Percentage spent by category\n"
    perc = []
    longest = -1
    tot_wintdraws = 0

    for i in categories:
        tot_wintdraws += i.withdraws
    
    for i in categories:
        temp = (i.withdraws / tot_wintdraws) * 100
        temp = temp - (temp % 10) # Arrotondamento per difetto alla decina: 29>20, 10>10
        perc.append(temp) # [%%, %%, %%]

        if len(i.name) > longest:
            longest = len(i.name)

    p = 100
    while p >= 0:
        temp = str(p) + "| "
        s += "{:>5}".format(temp)
        for n in perc:
            if n < p:
                s += "   "
            else:
                s += "o  "
        
        s += "\n"
        p -= 10
    
    # Divisore
    s += "    -"
    for o in perc: s += "---" 
    s += "\n"

    # Cat names
    char = 0
    while(char < longest):
        s += "     "
        for cat in categories:
            if char < len(cat.name):
                s += cat.name[char] + "  "
            else:
                s += "   "
        if char < (longest-1): # Avoid last \n
            s += "\n"
        char += 1
    
    return s