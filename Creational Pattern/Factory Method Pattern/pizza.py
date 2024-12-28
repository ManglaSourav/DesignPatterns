
class Pizza:
    
    def prepare(self):
        raise Exception("Can not prepare pizza here")
    
    def bake(self):
        print("Baking for 10 minutes")
        
    def cut(self):
        print("Cutting the pizza")
        
    def box(self):
        print("Boxing the pizza")
        
        
class CheesePizza(Pizza):
    
    def prepare(self):
        print("Preparing cheese pizza")
        

class VeggiePizza(Pizza):

    def prepare(self):
        print("Preparing Veggie pizza")
