import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if len(sys.argv) > 1:
        dict = {}
        for items in sys.argv[1:]:
            dict[items.split(":")[0]] = items.split(":")[1]
        #print(dict)
        total_items = 0
        unique_items = 0
        for x in dict.values():
            total_items += int(x)
            unique_items += 1
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item Types: {unique_items}")
        print()
        print("=== Current Inventory ===")
        for x, y in dict.items():
            print(f"{x}: {y} units ({((int(y) / total_items) * 100):.2f})")
        
        print()

        print("=== Inventory Statistics ===")
        list_items = []
        for x in dict.values():
            list_items.append(x)
        
        most_abundant = max(list_items)
        least_abundant = min(list_items)
        print(f"Most abundant: {max(dict, key=dict.get)} ({most_abundant} units)")
        print(f"Least abundant: {min(dict, key=dict.get)} ({least_abundant} units)")

        print()

        print("=== Item Categories ===")
        moderate_dic = {}
        scarce_dic = {}
        for x, y in dict.items():
            if int(y) > 3:
                moderate_dic[x] = y
            else:
                scarce_dic[x] = y
        print(f"Moderate: {moderate_dic}")
        print(f"Scarce: {scarce_dic}")

        print()

        print("=== Management Suggestions ===")
        restock_list = []
        for x, y in dict.items():
            if int(y) == 1:
                restock_list.append(x)
        print(f"Restock needed: {restock_list}")

        print()

        print("=== Dictionary Properties Demo ===")
        print(f"Dictionnary keys: {dict.keys()}")
        print(f"Dictionnary values: {dict.values()}")
        if dict["sword"]:
            print("Sample lookup - 'sword' in inventory: True")
                        

