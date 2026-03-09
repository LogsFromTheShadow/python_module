"""
Garden Plant Growth.
Demonstrates instance methods, modifying instance attributes,
and simulating state changes over time.
"""


class Plant:
    """
    A class representing a plant.
    Demonstrates how instance methods can modify the internal state
    (attributes) of an object.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """Instance method to increase the plant's height."""
        self.height += 1

    def increase_age(self) -> None:
        """
        Instance method to increase the plant's age.
        """
        self.age += 1

    def get_info(self) -> None:
        """Displays the current state of the plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    initial_height = plant.height

    print("=== Day 1 ===")
    plant.get_info()

    # Simulate growth for 6 days to reach Day 7
    for _ in range(6):
        plant.grow()
        plant.increase_age()

    print("=== Day 7 ===")
    plant.get_info()
