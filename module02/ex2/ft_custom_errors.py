class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def verify_plants():
    raise PlantError("The tomato plant is wilting!")


def verify_water():
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        verify_plants()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        verify_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")

    try:
        verify_plants()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        verify_water()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("All custom error types work correctly")