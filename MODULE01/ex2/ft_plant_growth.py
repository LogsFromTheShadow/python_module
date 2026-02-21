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
        Renamed from 'Age' to respect snake_case conventions and avoid
        conflict with the 'age' instance attribute.
        """
        self.age += 1

    def get_info(self) -> None:
        """Displays the current state of the plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)

    count: int = 1
    for x in range(1, 7):
        print(f"=== Day {count} ===")
        plant1.get_info()
        plant1.grow()
        plant1.increase_age()
        count += 1

    print(f"=== Day {count} ===")
    print(f"Growth this week: +{count - 1}cm")
