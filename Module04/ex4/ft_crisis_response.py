def handle_archive_access(filename, is_routine=False):
    if is_routine:
        alert_prefix = "ROUTINE ACCESS"
    else:
        alert_prefix = "CRISIS ALERT"

    print(f"{alert_prefix}: Attempting access to '{filename}'...")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Crisis handled, system stabilized")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    handle_archive_access('lost_archive.txt')
    handle_archive_access('classified_vault.txt')
    handle_archive_access('standard_archive.txt', is_routine=True)
    print("All crisis scenarios handled successfully. Archives secure.")
