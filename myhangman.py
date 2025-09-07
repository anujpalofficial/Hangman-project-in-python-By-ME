# this is my first python project and I take two days to create this with full fucntionality still , I think I can modify this game into more fun by adding level: like easy ,medium, hard. BTW thanks for checking out.
import random
import string
word_list = ["apple","banana","python","hangman","water","cloud","happy","tiger","phone","music","smile","dance","earth","dream","river"]
HANGMANPICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def choosen_word():
    return random.choice(word_list).lower()

def show_current(word,guessed):
    return ' '.join([c if c in guessed else '_' for c in word])
name = input("Enter your good name:")
def play():
    word = choosen_word()
    guessed = set()
    wrong = 0
    max_wrong = len(HANGMANPICS)-1

    print(f"\nWelcome {name} to the Hangman Game")
    while True:
        print(HANGMANPICS[wrong])
        print("Word:",show_current(word,guessed))
        print("Guessed:",' '.join(sorted(guessed) if guessed else "(none)"))
        print("Attempts left:",max_wrong-wrong)
        guess = input("Guess a letter or complete word:").strip().lower() 

        if not guess:
            print("type a letter or word")
            continue
        if not all(ch in string.ascii_letters for ch in guess):
            print("please use letters only")
            continue

        if len(guess) > 1:
            if guess == word:
                print("Great job,you guessed the completer word")
                break
            else:
                wrong += 1
                print("No that's not the word")
        else:
            letter = guess
            if letter in guessed:
                print("already guessed",letter)
                continue
            guessed.add(letter)
            if letter in word:
                print(f"The letter is in word")
            else:
                wrong +=1
                print("This letter is not in the word")
        if all(c in guessed for c in word):
            print("\n" + show_current(word,guessed))
            print("congratulations you uncovered the word")
            break
        if wrong >= max_wrong:
            print(HANGMANPICS[wrong])
            print("game over the word was:",word)
            break
if __name__  == "__main__":
    while True:
        play()
        again = input("type 'y' too play 'n' to exit:")
        if again != "y":
            print("Thanks for playing")
            break        

            
                


