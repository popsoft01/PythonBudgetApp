import Budgeting_App
from unittest import main

food = Budgeting_App.Budget("Food")
food.deposit(100, "initial deposit")
food.withdraw(20.0, "groceries")
food.check_fund(200)
print(food.check_balance())
clothing = Budgeting_App.Budget("clothing")
clothing.transfer(100, clothing)
clothing.withdraw(100)
food.check_fund(200)
print(food.check_balance())

print(food)
print(clothing)
