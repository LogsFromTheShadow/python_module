if __name__ == "__main__":
    with open("new_discovery.txt", "w+") as f:
        content = ("[ENTRY 001] New quantum algorithm discovered\n"
                   "[ENTRY 002] Efficiency increased by 347%\n"
                   "[ENTRY 003] Archived by Data Archivist trainee")
        f.write(content)

        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        print()
        print("Initializing new storage unit: new_discovery.txt")
        print("Storage unit created successfully...")
        print()
        print("Inscribing preservation data...")
        f.seek(0)
        print(f.read())
        print()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
