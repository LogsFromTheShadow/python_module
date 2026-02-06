def water_plants(plant_list):
    print("Opening watering system")

    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")

            print(f"Watering {plant}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!")

    print()

    print("Testing with error...")
    bad_plants = ["tomato", None]
    water_plants(bad_plants)
    print("Cleanup always happens, even with errors")

if __name__ == "__main__":
    test_watering_system()
