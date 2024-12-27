

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_method = None

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def cart_checkout(self):
        total = 0

        for i in range(len(self.items)):
            total += self.items[i]["price"]

        if self.payment_method:
            print("Total amount is $", total)
            self.payment_method.pay(total)
        else:
            print("Please confirm your payment method!")

    def add_item(self, item):
        self.items.append(item)

    def view_cart(self):
        print("Your cart contains:")
        for i in range(len(self.items)):
            name, price = self.items[i]["name"], self.items[i]["price"]
            print(f'{i}. {name} - {price}')
