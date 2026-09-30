import random
import sys


def get_target_points() -> int:
    while True:
        raw_input = input("Enter target points to win (or 'q' to quit): ").strip()
        if raw_input.lower() == "q":
            print("\nExiting game. Goodbye!")
            sys.exit(0)
        try:
            points = int(raw_input)
            if points > 0:
                return points
            print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_rock_paper_scissors():
    print("=" * 45)
    print("      🎮 ROCK · PAPER · SCISSORS (CLI)")
    print("=" * 45)

    target_points = get_target_points()

    point_hi = 0
    point_ai = 0

    choices_map = {"1": "rock", "2": "paper", "3": "scissor"}
    icons = {"rock": "🪨", "paper": "📄", "scissor": "✂️"}

    print(f"\n--- Match Started! First to {target_points} wins! ---")

    while point_hi < target_points and point_ai < target_points:
        print(f"\nScore -> You: {point_hi} | AI: {point_ai} (Target: {target_points})")
        print("Choose: [1] Rock 🪨   [2] Paper 📄   [3] Scissors ✂️   [Q] Quit")

        user_cmd = input("Your choice: ").strip().lower()

        if user_cmd in ("q", "quit"):
            print("\nMatch abandoned. Goodbye!")
            return

        if user_cmd not in choices_map:
            print("Invalid selection! Please enter 1, 2, 3, or Q.")
            continue

        player_choice = choices_map[user_cmd]
        ai_choice = random.choice(["rock", "paper", "scissor"])

        print(
            f"\nYou chose: {player_choice.title()} {icons[player_choice]}  |  "
            f"AI chose: {ai_choice.title()} {icons[ai_choice]}"
        )

        if player_choice == ai_choice:
            print(">> It's a Tie! 🤝")
        elif (
            (player_choice == "rock" and ai_choice == "scissor")
            or (player_choice == "paper" and ai_choice == "rock")
            or (player_choice == "scissor" and ai_choice == "paper")
        ):
            print(">> You Win This Round! 🎉")
            point_hi += 1
        else:
            print(">> AI Wins This Round! 🤖")
            point_ai += 1

    print("\n" + "=" * 45)
    if point_hi == target_points:
        print("         🏆 YOU WON THE MATCH! 🏆")
    else:
        print("          💀 AI WON THE MATCH! 💀")
    print(f"       Final Score -> You: {point_hi} | AI: {point_ai}")
    print("=" * 45)


if __name__ == "__main__":
    while True:
        play_rock_paper_scissors()
        again = input("\nPlay another match? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break