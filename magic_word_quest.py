# Magic Word Quest 🐍

def play_game():
    magic_word = "dream"  # The magic word to guess
    attempts = 0  # Counter for attempts
    max_attempts = 3  # Maximum allowed attempts

    print("Welcome to Magic Word Quest!")
    print(f"Hint: The word has {len(magic_word)} letters and starts with '{magic_word[0]}'.")

    while attempts < max_attempts:
        word = input("Enter your guess: ")
        attempts += 1

        if word == magic_word:
            print("Congratulations! You guessed the magic word! 🎉")
            break
        else:
            print("Incorrect. Try again.")
            print(f"Attempts left: {max_attempts - attempts}")

    if word != magic_word:
        print(f"Game over. The magic word was '{magic_word}'. Better luck next time!")

# Call the function to start the game
play_game()
