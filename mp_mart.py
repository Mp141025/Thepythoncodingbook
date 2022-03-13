# # less than operator < using __lt__()
# less than or equal operator <= using __le__()
# greater than or equal operator >= using __ge__()
# equality operator == using __eq__()

# You can try out __sub__() and __mul__() too!

# There are many other dunder methods that allow 
# you to customise your class and how it behaves.
#  For example, there is a dunder method to make a 
#  data type an iterable and another to make it 
#  indexable.

class Product:
    def __init__(self, name, cost_price, selling_price, number_in_stock):
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.number_in_stock = number_in_stock

    def decrease_stock(self, quantity):
        self.number_in_stock -= quantity

    def change_cost_price(self, new_price):
        self.cost_price = new_price

    def change_selling_price(self, new_price):
        self.selling_price = new_price


    def show_stock(self):
        print(f"{self.name} | Number in stock: {self.number_in_stock}")

    def __str__(self):
        return f"{self.name} | Selling Price: £{self.selling_price:.2f}"

    def __gt__(self, other):
        return self.selling_price > other.selling_price

    def __add__(self, other):
        return self.selling_price + other.selling_price
    
class CashRegister:
    def __init__(self):
        self.income = 0
        self.profit = 0
        self.cash_available = 100
    def register_sale(self, item: Product, quantity: int):
        sale_amount = quantity * item.selling_price
        self.income += sale_amount
        self.cash_available += sale_amount
        self.profit += quantity * (item.selling_price - item.cost_price)
        item.decrease_stock(quantity)
        


class Sandwich(Product):
    def __init__(self, filling, cost_price, selling_price, number_in_stock):
        super().__init__("Sandwich", cost_price, selling_price, number_in_stock)
        self.filling = filling

    def __str__(self):
        return f"{self.filling} sandwich | Selling Price: £{self.selling_price:.2f}"