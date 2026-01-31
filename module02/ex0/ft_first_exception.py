def check_temperature(temp_str):
    try:
        print(f"Testing Temperature: {temp_str}")
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    except Exception:
        print(f"Error: {temp_str} is not a valid number")


def test_temperature_input():
    check_temperature("abc")
    check_temperature("123")
    check_temperature("-50")
    check_temperature("34")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print("")
    test_temperature_input()
    print()
    print("All tests completed - program didn't crash!")
