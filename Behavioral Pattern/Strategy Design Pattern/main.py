
from shopping_cart import ShoppingCart

from payment_strategy import UPI, Card, InternetBanking, Cash


shopping_cart = ShoppingCart()

shopping_cart.add_item({"name": "Mobile", "price": 1000})
shopping_cart.add_item({"name": "PS5", "price": 500})
shopping_cart.add_item({"name": "Laptop", "price": 1400})

shopping_cart.view_cart()

shopping_cart.set_payment_method(Cash())
shopping_cart.cart_checkout()


shopping_cart.set_payment_method(UPI(11223434345, 1232343))
shopping_cart.cart_checkout()


shopping_cart.set_payment_method(Card(1232342453242, 123244))
shopping_cart.cart_checkout()
