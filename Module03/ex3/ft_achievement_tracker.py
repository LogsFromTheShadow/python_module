if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice_set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_set = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                   'perfectionist'}
    print(f"Player alice achievements: {alice_set}")
    print(f"Player bob achievements: {bob_set}")
    print(f"Player charlie achievements: {charlie_set}")

    print()
    print("=== Achievement Analytics ===")
    unique_achievement = alice_set | bob_set | charlie_set
    print(f"All unique achievement: {unique_achievement}")
    print(f"Total unique achievements: {len(unique_achievement)}")
    print()
    common_achievements = alice_set & bob_set & charlie_set
    print(f"Common to all players: {common_achievements}")
    r1_achievement = bob_set - alice_set - charlie_set
    r2_achievement = charlie_set - bob_set - alice_set

    rare_achievements = r1_achievement | r2_achievement
    print(f"Rare achievements (1 player): {rare_achievements}")
    print()
    alice_bob_commun = alice_set & bob_set
    alice_unique = alice_set - bob_set
    bob_unique = bob_set - alice_set

    print(f"Alice vs Bob common: {alice_bob_commun}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
