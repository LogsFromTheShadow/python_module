if __name__ == "__main__":
    scores = {"alice": 2300, "bob": 1800, "charlie": 2150, "diana": 2000}
    active = {"alice": True, "bob": True, "charlie": True, "diana": False}
    achs = {"alice": 5, "bob": 3, "charlie": 7, "diana": 2}
    cats = ["high", "high", "high", "medium", "medium", "low"]
    all_p = ["alice", "bob", "charlie", "diana", "alice"]
    ach_names = ["first_kill", "level_10", "boss_slayer", "first_kill"]
    regs = ["north", "east", "central", "north"]
    p_achs = {
        "alice": {"a1", "a2", "a3", "a4", "a5"},
        "bob": {"a6", "a7", "a8"},
        "charlie": {"a9", "a10", "a11", "a12"},
    }

    print("=== Game Analytics Dashboard ===")

    print("=== List Comprehension Examples ===")
    high_s = [k for k, v in scores.items() if v > 2000]
    doubled = [v * 2 for v in scores.values()]
    act_p = [k for k, v in active.items() if v]

    print(f"High scorers (>2000): {high_s}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {act_p}")

    print("=== Dict Comprehension Examples ===")
    p_scores = {k: v for k, v in scores.items() if k != "diana"}
    s_cats = {c: cats.count(c) for c in ("high", "medium", "low")}
    ach_cnts = {k: v for k, v in achs.items() if k != "diana"}

    print(f"Player scores: {p_scores}")
    print(f"Score categories: {s_cats}")
    print(f"Achievement counts: {ach_cnts}")

    print("=== Set Comprehension Examples ===")
    u_players = {p for p in all_p}
    u_achs = {a for a in ach_names}
    a_regs = {r for r in regs}

    print(f"Unique players: {u_players}")
    print(f"Unique achievements: {u_achs}")
    print(f"Active regions: {a_regs}")

    print("=== Combined Analysis ===")
    tot_players = len(u_players)
    all_u_achs = {a for val in p_achs.values() for a in val}
    avg_score = sum(scores.values()) / len(scores)
    top_p = max(scores, key=scores.get)

    print(f"Total players: {tot_players}")
    print(f"Total unique achievements: {len(all_u_achs)}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_p} ({scores[top_p]} points, "
          f"{achs[top_p]} achievements)")
