class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguemtns
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        # print(f'An instance created: {name}')
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def cal_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

print(Item.pay_rate)
# print(Item.__dict__) # All the attributes for Class Level


item1 = Item('Phone', 100, 1)
print(item1.__dict__) # All the attributes for instance level
# print(item1.name)
# print(item1.price)
# print(item1.quantity)
print(item1.pay_rate)
print(item1.cal_total_price())
item1.apply_discount()
print(item1.price)

item2 = Item('Laptop', 1000, 3)
print(item2.__dict__)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)
print(item2.pay_rate)
print(item2.cal_total_price())
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)