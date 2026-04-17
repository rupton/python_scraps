import random

def guess_number():
    number = random.randint(1,100)
    print("I am thinking of a number between 0 and 100. Your task is to guess it")
    while True:
        guess = int(input("What is your guess? "))
        
        if 1 <= guess <= 100:
            #check value
            if guess < number:
                print(f"Your guess {guess} is too low")
            elif guess > number:
                print(f"Your guess {guess} was too high")
            elif guess == number:
                print(f"Congratulations, you guessed {guess} which is the number I was thinking")
                break
        elif guess == 101:
            print(f"You found the secret cheat code. I was thinking of {number}")
        else:
            print(f"Your guess {guess} is not a number between 1 and 100")
            

guess_number()
        