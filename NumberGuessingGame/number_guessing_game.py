import random

def playGame(number):

    # Select Difficulty Level
    print("Please select the difficulty level:\n"
          "1. Easy (10 chances)\n"
          "2. Medium (5 chances)\n"
          "3. Hard (3 chances)\n")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    chances = 10
                    print("Great! You have selected the Easy Level")
                    break
                case 2:
                    chances = 5
                    print("Great! You have selected the Medium Difficulty Level")
                    break
                case 3:
                    chances = 3
                    print("Great! You have selected the Hard Level")
                    break
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number.")

    # Game starts
    print("Let's start the game!\n")

    for i in range(chances):
        try:
            guess_number = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess_number > number:
            print(f"Incorrect! The number is less than {guess_number}.\n")
        elif guess_number < number:
            print(f"Incorrect! The number is greater than {guess_number}.\n")
        elif guess_number == number:
            print(f"🎉 Congratulations! You guessed the correct number in {i+1} attempt(s).")
            break
    else:
        print("❌ Game over! All chances are used up — better luck next time!")
        print(f"The correct number is {number}")

def main():

    # Welcome Message
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Select a Random Number between 1 to 100
    number = random.randint(1,100)

    # Play the game
    playGame(number)
    
if __name__ == "__main__":
    main()