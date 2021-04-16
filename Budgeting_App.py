class Budget:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, category, description=""):

        if self.check_fund(amount):
            self.ledger.append({"amount": amount, "description": description, "category":category})
            return True
        return False

    def check_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]

    def transfer(self, amount, category):
        if self.check_fund(amount):
            self.withdraw(amount, " Transfer to ",category.name)
            category.deposit(amount, " transfer from ", self.name)
            return True
        return False

    def check_fund(self, amount):
        if self.check_balance() >= amount:
            return True
        return False


if __name__ == "__main__":
    Budget()
