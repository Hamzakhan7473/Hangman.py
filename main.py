from word_selector import get_random_word
from display import initialize_display, update_display, print_display
from game_logic import is_guess_valid, check_win, check_loss
from ascii_art import print_stage

def main():
    word = get_random_word()
    display = initialize_display(word)
    guessed_letters = []
    wrong_attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!\n")

    while True:
        print_display(display)
        guess = input("Enter your guess: ").lower()

        if not is_guess_valid(guess, guessed_letters):
            print("Invalid or repeated guess.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            display = update_display(word, display, guess)
        else:
            wrong_attempts += 1
            # print_stage(wrong_attempts)
            print(f"Wrong guess! Attempts left: {max_attempts - wrong_attempts}")

        if check_win(display):
            print_display(display)
            print("🎉 You win!")
            break
        elif check_loss(wrong_attempts, max_attempts):
            print(f"😵 You lose! The word was '{word}'")
            break

if __name__ == "__main__":
    main()
    