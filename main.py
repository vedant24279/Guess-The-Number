import random
logo = r'''
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
'''
print("Welcome to the Number Guessing Game.".center(100))
print(logo)
print("I am thinking of a number between 1 to 100.")
Difficulty = str(input("Choose Difficulty. Type 'Easy' or 'Hard' : ".lower()))
Random_Number = random.randrange(1,100)
def difficulty(level):
    if level == "easy":
        i = 10
    else:
        i = 5
    while i >= 1 :
        print(f"You have {i} attemps remaining to guess the number.")
        Guess = int(input("Make a Guess : "))
        if Guess == Random_Number :
            print(f"You got it! The answer was {Guess}")
            break
        elif Guess > Random_Number :
            print("Too High")
            print("Guess Again")
            i = i - 1
            if i == 0 :
                    print("You ran out of guesses.")
                    exit()
        elif Guess < Random_Number :
            print("Too Low")
            print("Guess Again")
            i = i - 1
            if i == 0 :
                    print("You ran out of guesses.")
                    exit()

difficulty(Difficulty)