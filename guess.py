"""A simple number-guessing game.

Run it with:  python guess.py
"""

import random


def play(low: int = 1, high: int = 100) -> int:
    """Play one round and return how many guesses it took."""
    secret = random.randint(low, high)
    attempts = 0
    print(f"I'm thinking of a number between {low} and {high}.")

    while True:
        raw = input("Your guess: ").strip()
        if not raw.lstrip("-").isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(raw)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} guesses.")
            return attempts


def main() -> None:
    best = None
    while True:
        attempts = play()
        if best is None or attempts < best:
            best = attempts
            print("New best score!")
        print(f"Best so far: {best} guesses.")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
