import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():

    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistake = 0
    guessed_letters = []
    # For now, simply prompt the user once:

    while True:

        while True:
            guess = input("Guess a letter: ").lower().strip()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter single letter (a-z)")
                continue

            print("You guessed:", guess)
            break

        guessed_letters.append(guess)
        if guess not in secret_word:
            mistake += 1
        display_game_state(mistake, secret_word, guessed_letters)

        if mistake >= len(STAGES) - 1:
            print(f"Game Over! The word was: {secret_word}")
            break

        elif all(letter in guessed_letters for letter in secret_word):
            print("Congratulations, you saved the snowman!")
            break

    ask_play_again()


def display_game_state(mistakes, secret_word, guessed_letters):

    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_"
    print("Word:", display_word.strip())


def ask_play_again():

    game_cont = input("Do you want to play again? (y/n)").lower()
    if game_cont == "y":
        play_game()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    play_game()
