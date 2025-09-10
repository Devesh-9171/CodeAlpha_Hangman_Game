import random

def display_hangman(incorrect_guesses):
    """Display hangman figure based on number of incorrect guesses"""
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    return stages[incorrect_guesses]

def hangman_game():
    """Main hangman game function"""
    # List of 5 predefined words
    words = ["python", "programming", "computer", "keyboard", "screen"]
    
    # Randomly select a word
    word = random.choice(words).lower()
    word_letters = set(word)  # Letters in the word
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()  # What the user has guessed
    
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("🎮 WELCOME TO HANGMAN! 🎮")
    print("=" * 40)
    print("Guess the word one letter at a time.")
    print(f"The word has {len(word)} letters.")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    print("Good luck!\\n")
    
    # Game loop
    while len(word_letters) > 0 and incorrect_guesses < max_incorrect_guesses:
        # Display hangman figure
        print(display_hangman(incorrect_guesses))
        
        # Show current progress
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(f"Word: {' '.join(word_list)}")
        print(f"Used letters: {' '.join(sorted(used_letters))}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        print("-" * 40)
        
        # Get user input
        user_letter = input("Guess a letter: ").lower().strip()
        
        # Validate input
        if len(user_letter) != 1:
            print("⚠️  Please enter only one letter.\\n")
            continue
        elif user_letter not in alphabet:
            print("⚠️  Please enter a valid letter.\\n")
            continue
        elif user_letter in used_letters:
            print("⚠️  You have already used that letter. Try again.\\n")
            continue
        
        # Process the guess
        used_letters.add(user_letter)
        
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print(f"✅ Excellent! '{user_letter}' is in the word!\\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry, '{user_letter}' is not in the word.\\n")
    
    # Game end
    print(display_hangman(incorrect_guesses))
    final_word = ' '.join([letter if letter in used_letters else '_' for letter in word])
    print(f"Final word: {final_word}")
    
    if len(word_letters) == 0:
        print("🎉 CONGRATULATIONS! 🎉")
        print(f"You guessed the word '{word}' correctly!")
        print("You're a Hangman champion!")
    else:
        print("💀 GAME OVER! 💀")
        print(f"The word was '{word}'.")
        print("Better luck next time!")

def play_again():
    """Ask if player wants to play again"""
    while True:
        choice = input("\\nDo you want to play again? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

# Main program
if __name__ == "__main__":
    print("🎯 HANGMAN GAME 🎯")
    print("A classic word guessing game!")
    print("Guess the mystery word before the hangman is complete!\\n")
    
    while True:
        hangman_game()
        if not play_again():
            print("\\nThanks for playing Hangman! Goodbye! 👋")
            break


# Save the complete game to a file
with open('hangman_game.py', 'w') as f:
    f.write(hangman_code)

print("✅ Complete Hangman Game created successfully!")
print("\nFile saved as: hangman_game.py")
print("\n📋 GAME FEATURES:")
print("• 5 predefined words: python, programming, computer, keyboard, screen")
print("• Maximum 6 incorrect guesses")
print("• ASCII hangman figure display")
print("• Input validation")
print("• Play again option")
print("• Text-based console interface")
print("\n🎮 TO RUN THE GAME:")
print("1. Save the code to a file called 'hangman_game.py'")
print("2. Run: python hangman_game.py")
print("3. Follow the on-screen prompts to play!")