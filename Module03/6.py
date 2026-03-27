if __name__ == "__main__":
    scores = {"alice": 2300, "bob": 1800, "charlie": 2150, "diana": 2000}
    active_player = {"alice": True, "bob": True, "charlie": True, "diana": False}
    score_cat = ["high", "high", "high", "medium", "medium", "low"]
    player_achievements = {"alice": 5, "bob": 3, "charlie": 7}
    all_players = {"alice", "bob", "charlie", "diana", "bob"}
    achievement = {"first kill", "level_10", "boss slayer", "level_10"}
    regions = {"north": True, "east": True, "central": True, "west": False}
    p_achs = {
        "alice": {"a1", "a2", "a3", "a4", "a5"},
        "bob": {"a6", "a7", "a8"},
        "charlie": {"a9", "a10", "a11", "a12"},
    }


    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")

    high_scorers = [x for x, y in scores.items() if y >= 2000]
    Score_doubled = [x * 2 for x in scores.values()]
    player_active = [x for x, y in active_player.items() if y ]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled:{Score_doubled}")
    print(f"Active Players: {player_active}")

    print()

    print("=== Dict Comprehension Examples ===")
    player_scores = {x: y for x, y in scores.items() if x != "diana"}
    score_categories = {x: score_cat.count(x) for x in ("high", "medium", "low")}
    ach_counts = {x: y for x, y in player_achievements.items()}
    print(f"player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {ach_counts}")

    print()

    print("=== Set Comprehension Examples ===")
    unique_playes = {x for x in all_players}
    unique_achievement = {x for x in achievement}
    active_regions = {x for x, y in regions.items() if y}
    print(f"Unique players: {unique_playes}")
    print(f"unique achievement: {unique_achievement}")
    print(f"Active regions: {active_regions}")

    print()

    print("=== Combined Analysis===")
    print(f"total players:{len(unique_playes)}")
    all_unique_ach = {x for val in p_achs.values() for x in val}
    average_score = sum(scores.values()) / len(scores)
    top_player = max(scores, key=scores.get)

    print(f"Totoal unique achievement: {len(all_unique_ach)}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_player} ({scores[top_player]},"
          f" {player_achievements[top_player]})")
