def is_guess_valid(guess, guessed_letters):
   return guess.isalpha() and len(guess) == 1 and guess not in guessed_letters

def check_win(display):
    return "_" not in display

def check_loss(wrong_attempts, max_attempts):
    return wrong_attempts >= max_attempts