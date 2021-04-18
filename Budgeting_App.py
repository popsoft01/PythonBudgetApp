class Budget:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f"{self.name:*^30}\n"

        total = 0
        for item in self.ledger:
            item += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']
            output = title + item + "total:" + total
            return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):

        if self.check_fund(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def check_balance(self) -> float:
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
            return total_cash
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
