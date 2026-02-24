import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        inventory = {}
        for x in sys.argv[1:]:
            parts = x.split(":")
            inventory[parts[0]] = int(parts[1])

        print("=== Inventory System Analysis ===")
        total_items = sum(inventory.values())
        unique_items = len(inventory.keys())

        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {unique_items}\n")

        print("=== Current Inventory ===")
        items_list = []
        for k, v in inventory.items():
            items_list.append((k, v))

        n = len(items_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if items_list[j][1] < items_list[j + 1][1]:
                    temp = items_list[j]
                    items_list[j] = items_list[j + 1]
                    items_list[j + 1] = temp

        for key, value in items_list:
            unit_word = "units" if value > 1 else "unit"
            percentage = (value / total_items) * 100
            print(f"{key}: {value} {unit_word} ({percentage:.1f}%)")
        print()

        print("=== Inventory Statistics ===")
        most_ab = max(inventory, key=inventory.get)
        least_ab = min(inventory, key=inventory.get)

        most_val = inventory[most_ab]
        least_val = inventory[least_ab]

        w_most = "units" if most_val > 1 else "unit"
        w_least = "units" if least_val > 1 else "unit"

        print(f"Most abundant: {most_ab} ({most_val} {w_most})")
        print(f"Least abundant: {least_ab} ({least_val} {w_least})\n")

        print("=== Item Categories ===")
        categories = {"Moderate": dict(), "Scarce": dict()}

        for key, value in inventory.items():
            if value >= 5:
                categories["Moderate"].update({key: value})
            else:
                categories["Scarce"].update({key: value})

        print(f"Moderate: {categories['Moderate']}")
        print(f"Scarce: {categories['Scarce']}\n")

        print("=== Management Suggestions ===")
        restock_str = ""
        is_first = True
        for k, v in inventory.items():
            if v == 1:
                if not is_first:
                    restock_str += ", "
                restock_str += k
                is_first = False
        print(f"Restock needed: {restock_str}\n")

        print("=== Dictionary Properties Demo ===")
        keys_str = ""
        is_first = True
        for k in inventory.keys():
            if not is_first:
                keys_str += ", "
            keys_str += k
            is_first = False

        values_str = ""
        is_first = True
        for v in inventory.values():
            if not is_first:
                values_str += ", "
            values_str += str(v)
            is_first = False

        print(f"Dictionary keys: {keys_str}")
        print(f"Dictionary values: {values_str}")
        is_present = 'sword' in inventory
        print(f"Sample lookup - 'sword' in inventory: {is_present}")