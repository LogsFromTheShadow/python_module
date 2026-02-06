def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name or not plant_name.strip():
        raise ValueError("Plant name cannot be empty.")

    if not 1 <= water_level <= 10:
        raise ValueError("Water level must be between 1 and 10.")

    if not 2 <= sunlight_hours <= 12:
        raise ValueError("Sunlight hours must be between 2 and 12.")

    return f"Success: {plant_name} is healthy."


def test_plant_checks():
    test_cases = [
        ("Rose", 5, 6),
        ("", 5, 6),
        ("Tulip", 15, 6),
        ("Cactus", 5, 1),
    ]

    for name, water, sun in test_cases:
        try:
            print(check_plant_health(name, water, sun))
        except ValueError as e:
            print(f"Error caught: {e}")


if __name__ == "__main__":
    test_plant_checks()
