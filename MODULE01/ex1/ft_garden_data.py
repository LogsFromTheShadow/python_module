class Plant:
    """
    A simple class representing a plant.
    Acts as a blueprint for creating plant objects with specific attributes.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Constructor method.
        Initializes a new Plant instance with a name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== garden Plant Registry ===")

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)

    plants: list[Plant] = [plant1, plant2, plant3]

    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
