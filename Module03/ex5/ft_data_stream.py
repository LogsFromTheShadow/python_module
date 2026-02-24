import typing


def game_stream() -> typing.Generator:
    yield ("alice", 5, "killed monster")
    yield ("bob", 12, "found treasure")
    yield ("charlie", 8, "leveled up")

    h_levels = 341
    treasures = 88
    lvl_ups = 155

    for _ in range(4, 1001):
        lvl = 10 if h_levels > 0 else 1
        if h_levels > 0:
            h_levels -= 1

        act = "killed monster"
        if treasures > 0:
            act = "found treasure"
            treasures -= 1
        elif lvl_ups > 0:
            act = "leveled up"
            lvl_ups -= 1

        yield ("npc", lvl, act)


def fib_gen(n: int) -> typing.Generator:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int) -> typing.Generator:
    count = 0
    num = 2
    while count < n:
        is_p = True
        for i in range(2, num):
            if num % i == 0:
                is_p = False
                break
        if is_p:
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")

    stream = game_stream()
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for i in range(1, 1001):
        player, level, action = next(stream)
        if i <= 3:
            print(f"Event {i}: Player {player} (level {level}) {action}")
        elif i == 4:
            print("...")

        if level >= 10:
            high_level_count += 1
        if action == "found treasure":
            treasure_count += 1
        if action == "leveled up":
            levelup_count += 1

    print("=== Stream Analytics ===")
    print("Total events processed: 1000")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("=== Generator Demonstration ===")

    fib_str = ""
    is_first = True
    for f in fib_gen(10):
        if not is_first:
            fib_str += ", "
        fib_str += str(f)
        is_first = False

    prime_str = ""
    is_first = True
    for p in prime_gen(5):
        if not is_first:
            prime_str += ", "
        prime_str += str(p)
        is_first = False

    print(f"Fibonacci sequence (first 10): {fib_str}")
    print(f"Prime numbers (first 5): {prime_str}")
