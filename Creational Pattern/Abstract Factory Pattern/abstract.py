

class Chair:
    def sit_on(self):
        raise Exception("Sitting on chair")


class Sofa:
    def lie_on(self):
        raise Exception("Lying on sofa")


# Concrete product for modernStyle
class ModernChair(Chair):
    def sit_on(self):
        print("Sitting on modern chair")


class ModernSofa (Sofa):
    def lie_on(self):
        print("Lying on modern sofa")


# Concrete product for classicStyle
class ClassicChair (Chair):
    def sit_on(self):
        print("Sitting on classic chair")


class ClassicSofa (Sofa):
    def lie_on(self):
        print("Lying on classic sofa")


# Abstract factory
class FurnitureFactory:
    def create_chair(self):
        raise Exception("Creating chair")

    def create_sofa(self):
        raise Exception("Creating sofa")


# Concrete factory for modernStyle
class ModernFurnitureFactory (FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


# Concrete factory for classicStyle


class ClassicFurnitureFactory (FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_sofa(self):
        return ClassicSofa()
