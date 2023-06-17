from product import *
from people import *
from student import *

# lists = []
# n = int(input("Enter N ="))
# for i in range(0, n):
#     id = int(input("Enter ID ="))
#     name = input("Enter Name =")
#     price = float(input("Enter Price =$"))
#     qty = float(input("Enter Quantity ="))
#     print("----------------------------")
#     p = Product(id, name, price, qty)
#     lists.append(p)
#
# grand_total = 0
# for product in lists:
#     grand_total += product.amount()
#     print(product)
#     print('=====================')
#
# print(f"\t\t grand total: {grand_total:,.2f}")

p = People(1, 'chantha', 25)
s = Student(2, 'pheak', 20, 'MIS', 5.0)
s.setSubject('Python')
s.setGpa(6.0)
print(s.getSubject())
print(s.getGpa())

print(p)
print(s)
