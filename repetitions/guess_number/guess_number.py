import random

target = random.randint(1, 100)

while True:
    guess = int(input())

    if guess < target:
        print("too low")
    elif guess > target:
        print("too high")
    else:
        print("correct!")
        break
