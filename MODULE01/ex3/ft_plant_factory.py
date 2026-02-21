class Plant:
    """
    A simple class representing a plant.
    Demonstrates the __init__ constructor method for initializing
    instance attributes.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


plants: list[tuple[str, int, int]] = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]


if __name__ == "__main__":
    count: int = 0
    print("=== Garden Plant Registry ===")

    for name, height, age in plants:
        plant = Plant(name, height, age)
        print(f"Created: {plant.name}: ({plant.height}cm, {plant.age} days)")
        count += 1

    print()
    print(f"Total plants created: {count}")
