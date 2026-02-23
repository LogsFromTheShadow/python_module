import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
    x = 1
    while x < len(sys.argv):
        print(f"Argument {x}: {sys.argv[x]}")
        x += 1
print(f"Total arguments: {len(sys.argv)}")
