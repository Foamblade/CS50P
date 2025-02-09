import random
while True:
    try:
        n = int(input("Level: "))
        break
    except:
        ...

x = random.randrange(1,10)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < x:
            print("Too small!")
        elif guess > x:
            print("Too large!")
        else:
            print("Just right!")
            break
    except:
        ...
