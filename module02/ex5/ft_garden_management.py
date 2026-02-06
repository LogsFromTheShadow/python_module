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
    def __init__(self):
        self.plants = []

    def add_plant(self, name, water, sun):
        """Adds a plant after validation."""
        if not name or not isinstance(name, str):
            raise PlantNameError("Plant name cannot be empty!")
        
        # On stocke la plante sous forme de dictionnaire simple
        plant = {
            "name": name,
            "water": int(water),
            "sun": int(sun)
        }
        self.plants.append(plant)
        print(f"Added {name} successfully")

    def water_plants(self):
        """Simulates watering with resource cleanup."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant['name']} - success")
                # Ici on pourrait simuler une erreur aléatoire
        except Exception as e:
            print(f"Error during watering: {e}")
        finally:
            # Ce bloc s'exécute TOUJOURS, même en cas d'erreur
            print("Closing watering system (cleanup)")

    def check_health(self):
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

    def trigger_tank_error(self):
        """Method specifically to test external error recovery."""
        raise GardenError("Not enough water in tank")


def test_garden_management():
    print("=== Garden Management System ===")
    garden = GardenManager()

    # 1. Adding plants
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
    except GardenError as e:
        print(f"Error: {e}")

    try:
        # On ajoute une laitue avec trop d'eau pour tester check_health plus tard
        garden.add_plant("lettuce", 15, 6)
    except GardenError as e:
        print(f"Error: {e}")

    try:
        # Test nom vide
        garden.add_plant("", 5, 5)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    # 2. Watering (Resource Management)
    print("Watering plants...")
    garden.water_plants()

    # 3. Checking Health
    print("Checking plant health...")
    garden.check_health()

    # 4. Error Recovery
    print("Testing error recovery...")
    try:
        garden.trigger_tank_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
