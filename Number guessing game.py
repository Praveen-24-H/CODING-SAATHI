import random

def play_guess_the_number():
    min_number = 1
    max_number = 100
    max_attempts = 10
    total_score = 0
    round_number = 1

    print("Welcome to the 'Guess the Number' Game!")

    while True:
        target_number = random.randint(min_number, max_number)
        attempts = 0

        print(f"\nRound {round_number}")
        print(f"I'm thinking of a number between {min_number} and {max_number}. Can you guess it?")

        while attempts < max_attempts:
            try:
                user_guess = int(input("Your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if user_guess < target_number:
                print("Go a bit higher!")
            elif user_guess > target_number:
                print("Try a little lower!")
            else:
                score = max_attempts - attempts + 1
                total_score += score
                print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
                print(f"Score for round {round_number}: {score} points")
                break

        if attempts >= max_attempts:
            print(f"Oops! You've used up all your attempts. The number was {target_number}.")

        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != "yes":
            break

        round_number += 1

    print(f"Total score: {total_score} points. Thanks for playing!")


play_guess_the_number()