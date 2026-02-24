if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established..")
    print()
    print("RECOVERED DATA:")
    with open("ancient_fragment.txt") as f:
        print(f.read())
    print()
    print("Data recovery complete. Storage unit disconnected.")
