class SecurePlant:
    """
    A class representing a plant with secure, private attributes.
    Direct access to height and age is restricted to prevent invalid data.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def get_height(self) -> int:
        """Getter method to safely access the private __height attribute."""
        return self.__height

    def get_age(self) -> int:
        """Getter method to safely access the private __age attribute."""
        return self.__age

    def set_height(self, x: int) -> None:
        """
        Setter method to safely update the private __height attribute.
        Includes validation to reject invalid types or negative values.
        """
        if not isinstance(x, int):
            print(f"Invalid operation attempted: height {x}cm [REJECTED]")
            x = self.__height
        if x < 0:
            print(f"Invalid operation attempted: height {x}cm [REJECTED]")
            print("Security: Negative age rejected")
            x = self.__height
        else:
            self.__height = x
            print(f"Height updated: {x}cm [OK]")

    def set_age(self, x: int) -> None:
        """
        Setter method to safely update the private __age attribute.
        Includes validation to reject invalid types or negative values.
        """
        if not isinstance(x, int):
            print(f"Invalid operation attempted: age {x} days [REJECTED]")
            x = self.__age
        if x < 0:
            print(f"Invalid operation attempted: age {x} days [REJECTED]")
            print("Security: Negative age rejected")
            x = self.__age
        else:
            self.__age = x
            print(f"Age updated: {x} days [OK]")

    def get_info(self) -> None:
        """Displays the current state of the plant."""
        print(f"Current plant: {self.name} ({self.get_height()}cm,"
              f" {self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("rose", 25, 30)
    print(f"Plant created: {plant.name}")
    print(f"Height updated: {plant.get_height()}cm [OK]")
    print(f"Age updated: {plant.get_age()} days [OK]")
    plant.set_height(-5)
    print()
    plant.get_info()
