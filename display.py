def initialize_display(word):
    return ["_"] * len(word)

def update_display(word, display, guess):
    for i, letter in enumerate(word):
        if letter == guess:
            display[i] = guess
    return display

def print_display(display):
    print(" ".join(display))