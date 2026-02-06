def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Vérifie la santé de la plante.
    Lève (raise) une ValueError si une donnée est invalide.
    Renvoie un message de succès si tout va bien.
    """

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        else:
            raise ValueError(f"Water level {water_level} is too low (min 1)")

    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        else:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 6)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
