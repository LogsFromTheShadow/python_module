import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        x = 0
        Score_list = []
        for score in sys.argv:
            try:
                Score_list.append(int(score))
            except ValueError:
                pass
        if len(Score_list) == 0:
            print("No valid scores provided. Usage: "
                  "python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            len_score_list = len(Score_list)
            total_score = sum(x for x in Score_list)
            min_score = min(Score_list)
            max_score = max(Score_list)

            print(f"Scores processed: {Score_list}")
            print(f"Total players: {len(Score_list)}")
            print(f"Total score: {total_score}")
            print(f"Average score: {float(total_score / len_score_list)} ")
            print(f"High score: {max_score}")
            print(f"Low score: {min_score}")
            print(f"Score range: {max_score - min_score}")
