from abstract import ModernFurnitureFactory, ClassicFurnitureFactory


def create_furniture(factory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    chair.sit_on()
    sofa.lie_on()


modern_factory = ModernFurnitureFactory()
create_furniture(modern_factory)

classic_factory = ClassicFurnitureFactory()
create_furniture(classic_factory)
