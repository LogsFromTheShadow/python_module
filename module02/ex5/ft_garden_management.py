from typing import Any


class GardenError(Exception):
    """Base class for garden exceptions."""
    pass


class PlantNameError(GardenError):
    """Raised when plant name is invalid."""
    pass


class PlantHealthError(GardenError):
    """Raised when plant stats are invalid."""
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[dict[str, Any]] = []

    def add_plant(self, name: str, water: int, sun: int) -> None:
        """Adds a plant after validation."""
        if not name or not isinstance(name, str):
            raise PlantNameError("Plant name cannot be empty!")

        plant = {
            "name": name,
            "water": int(water),
            "sun": int(sun)
        }
        self.plants.append(plant)
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Simulates watering with resource cleanup."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant['name']} - success")
        except Exception as e:
            print(f"Error during watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """Checks stats for all plants."""
        for plant in self.plants:
            try:
                if plant['water'] > 10:
                    raise PlantHealthError(
                        f"Water level {plant['water']} is too high (max 10)"
                    )
                if plant['sun'] < 2:
                    raise PlantHealthError(
                        f"Sun level {plant['sun']} is too low"
                    )

                print(f"{plant['name']}: healthy "
                      f"(water: {plant['water']}, sun: {plant['sun']})")
            except PlantHealthError as e:
                print(f"Error checking {plant['name']}: {e}")

    def trigger_tank_error(self) -> None:
        """Method specifically to test external error recovery."""
        raise GardenError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
    except GardenError as e:
        print(f"Error: {e}")

    try:
        garden.add_plant("lettuce", 15, 6)
    except GardenError as e:
        print(f"Error: {e}")

    try:
        garden.add_plant("", 5, 5)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    garden.water_plants()

    print("Checking plant health...")
    garden.check_health()

    print("Testing error recovery...")
    try:
        garden.trigger_tank_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
