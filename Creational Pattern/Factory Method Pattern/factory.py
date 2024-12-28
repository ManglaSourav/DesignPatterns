from pizza import VeggiePizza, CheesePizza


class PizzaFactory:

    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        if pizza_type == "veggie":
            return VeggiePizza()

        raise Exception("Invalid Pizza Type")
