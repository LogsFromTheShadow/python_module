
class Plant:
    """
    Base class representing common attributes of all plants.
    Serves as the parent class for specific plant types.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Demonstrates inheritance:
    Extends the Plant base class with flower-specific attributes (color)
    and behaviors (bloom).
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Method specific to the Flower class."""
        print(f"{self.name} is blooming beautifully")

    def get_flower_info(self) -> None:
        """Displays formatted information about the flower."""
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")


class Tree(Plant):
    """
    Demonstrates inheritance:
    Extends the Plant base class with tree-specific attributes
    (trunk_diameter) and behaviors (produce_shade).
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculates and displays the shade area based on trunk diameter."""
        shade_area = int((self.trunk_diameter / 2) * 3.14)
        print(f"{self.name} provides {shade_area} square meters of shade")

    def get_tree_info(self) -> None:
        """Displays formatted information about the tree."""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm trunk")


class Vegetable(Plant):
    """
    Demonstrates inheritance:
    Extends the Plant base class with vegetable-specific attributes
    (harvest_season, nutritional_value).
    """

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_veg_info(self) -> None:
        """Displays formatted information about the vegetable."""
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()

    flower1 = Flower("Rose", 25, 30, "red")
    tree1 = Tree("Oak", 500, 1825, 50)
    veg1 = Vegetable("Tomato", 80, 90, "summer", "C")

    flower2 = Flower("Sunflower", 80, 45, "yellow")
    tree2 = Tree("Noyer", 300, 1300, 25)
    veg2 = Vegetable("Carrot", 25, 45, "summer", "A")

    flower1.get_flower_info()
    flower1.bloom()
    print()

    tree1.get_tree_info()
    tree1.produce_shade()
    print()

    veg1.get_veg_info()
