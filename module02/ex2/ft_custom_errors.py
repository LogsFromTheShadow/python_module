class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


<<<<<<< HEAD
def arroser(litres):
    if litres < 0:
        raise WaterError("Impossible d'arroser avec une"
                         "quantité négative d'eau !")


try:
    arroser(-10)
except WaterError as e:
    print(f"erreur detecte: {e}")
=======
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
>>>>>>> 05625ada837f04550e5ae1e6ce2a3178503a4d29
