import random
import sys

CHOICES = {"r": "rock", "p": "paper", "s": "scissors"}
WIN_MAP = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}


def get_user_choice():
    prompt = "Choose (r)ock, (p)aper or (s)cissors: "
    while True:
        choice = input(prompt).strip().lower()
        if choice in CHOICES:
            return CHOICES[choice]
        # allow full word input too
        if choice in CHOICES.values():
            return choice
        print("Invalid choice. Enter r, p, s, rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(list(WIN_MAP.keys()))


def decide_winner(player, computer):
    if player == computer:
        return "tie"
    if WIN_MAP[player] == computer:
        return "player"
    return "computer"


def play_round():
    player = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose {player}. Computer chose {computer}.")
    winner = decide_winner(player, computer)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win this round!")
    else:
        print("Computer wins this round.")
    return winner


def best_of_n(n):
    needed = n // 2 + 1
    scores = {"player": 0, "computer": 0}
    round_num = 1
    while scores["player"] < needed and scores["computer"] < needed:
        print(f"\nRound {round_num} (first to {needed})")
        result = play_round()
        if result in scores:
            scores[result] += 1
        print(f"Score -> You: {scores['player']}  Computer: {scores['computer']}")
        round_num += 1
    if scores["player"] > scores["computer"]:
        print("\nYou won the match!")
    else:
        print("\nComputer won the match.")


def ask_best_of():
    while True:
        val = input("Play best-of how many rounds? (odd number, default 1): ").strip()
        if val == "":
            return 1
        if not val.isdigit():
            print("Please enter a positive odd integer (e.g. 1, 3, 5).")
            continue
        n = int(val)
        if n <= 0 or n % 2 == 0:
            print("Please enter a positive odd integer.")
            continue
        return n


def main():
    print("Rock Paper Scissors")
    while True:
        n = ask_best_of()
        if n == 1:
            play_round()
        else:
            best_of_n(n)
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
