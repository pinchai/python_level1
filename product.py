class Product:

    def __init__(self, id, name, price, qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty

    def amount(self):
        return self.price * self.qty

    def __str__(self):
        return f"{self.id}  {self.name}  " \
               f"{self.price:,.2f}  " \
               f"{self.qty:,.2f}  " \
               f"{self.amount():,.2f}"





