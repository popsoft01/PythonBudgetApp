class Budget:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total_balance = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total_balance += item['amount']
        output = title + items + "total balance:" + str(total_balance)
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):

        if self.check_fund(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def check_balance(self) -> float:
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
            return balance
        return False

    def transfer(self, amount, category):
        if self.check_fund(amount):
            self.withdraw(amount, " Transfer to " + category.name)
            category.deposit(amount, " transfer from " + self.name)
            return True
        return False

    def check_fund(self, amount) -> float:
        if self.check_balance() >= amount:
            return True
        return False

    def get_withdraw(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
                return total
