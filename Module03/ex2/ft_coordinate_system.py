import math


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    positions = (10, 20, 5)
    print(f"Position created: {positions}")
    formula = math.sqrt((positions[0] - 0)**2 + (positions[1] - 0)**2 +
                        (positions[2] - 0)**2)

    print(f"Distance between (0, 0, 0) and {positions}: {formula:.2f}")

    coordinates = "3,4,0"
    print(f'Parsing coordinates: "{coordinates}"')
    coord_list = coordinates.split(",")
    new_coord_list = []
    for x in coord_list:
        try:
            new_coord_list.append(int(x))
        except ValueError:
            pass

    tuple_coord_list = tuple(new_coord_list)
    formula2 = math.sqrt((tuple_coord_list[0] - 0)**2 +
                         (tuple_coord_list[1] - 0)**2 +
                         (tuple_coord_list[2] - 0)**2)

    print(f"Parsed position: {tuple_coord_list}")
    print(f"Distance between (0, 0, 0) and {tuple_coord_list}: {formula2}")

    invalid_coordinates = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_coordinates}"')
    inv_list = invalid_coordinates.split(",")

    for y in inv_list:
        try:
            int(y)
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
            break

    print("Unpacking demonstration:")
    x, y, z = tuple_coord_list
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
