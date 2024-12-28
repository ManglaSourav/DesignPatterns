

from factory import PizzaFactory


pizza_type = "cheese"
pizza = PizzaFactory.create_pizza(pizza_type)
pizza.prepare()
pizza.bake()
pizza.cut()
pizza.box()
