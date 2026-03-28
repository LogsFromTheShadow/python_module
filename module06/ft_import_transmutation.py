import alchemy.elements
import alchemy.potions
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water


if __name__ == "__main__":
    print("=== import transmutation Mastery ===")
    print()
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

    print()

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print()

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal}")

    print()

    print("Methos 4 - Multiple imports:")
    print(f"create_earth(): {alchemy.elements.create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {alchemy.potions.strength_potion()}")

    print()

    print("All import transmutation methods mastered!")