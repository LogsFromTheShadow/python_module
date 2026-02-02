def garden_operations(error):
    if error == "wrong data":
        int("abc")
    elif error == "zero_div":
        print(10 / 0)
    elif error == "file_error":
        open("missing.txt", "r")
    elif error == "key_error":
        garden = {"rose": 5}
        print(garden["tulipe"])


def error_types():
    print("=== Garden Error Types Demo ===")
    print("")
    try:
        print("Testing ValueError...")
        garden_operations("wrong data")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print("")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations("zero_div")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print("")

    try:
        print("Testing FileNotFoundError...")
        garden_operations("file_error")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print("")

    try:
        print("Testing KeyError...")
        garden_operations("key_error")
    except KeyError:
        print("Caught KeyError: missing_plant")
        print("")

    print("Testing multiple errors together...")
    print("Caught an error, but program continues!")
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    error_types()
