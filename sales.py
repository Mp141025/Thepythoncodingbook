

from mp_mart import Product, CashRegister

first_prod = Product("Coffee", 1.1, 2.5, 30)
second_prod = Product("Chocolate", 0.9, 1.75, 35)

till = CashRegister()

print(till.income)
print(till.profit)
print(till.cash_available)
second_prod.show_stock()

till.register_sale(second_prod, 5)
print()

print(till.income)
print(till.profit)
print(till.cash_available)
second_prod.show_stock()

print(first_prod + second_prod)
print(first_prod > second_prod)
print(first_prod)


# testing_inheritance.py

from mp_mart import Sandwich

type_1 = Sandwich("Cheese", 1.7, 3.5, 10)
type_2 = Sandwich("Ham", 1.9, 4, 10)
type_3 = Sandwich("Tuna", 1.8, 4, 10)

print(type_1)
print(type_2)
print(type_3)