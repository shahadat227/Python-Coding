import random

secret = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess number (1 - 10): "))

        if guess == secret:
            print("🎉 Correct!")
            break
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!")
    
    except:
        print("Enter a valid number!")

"""
output:
Guess number (1 - 10): 10
Too high!
Guess number (1 - 10): 5
🎉 Correct!
"""