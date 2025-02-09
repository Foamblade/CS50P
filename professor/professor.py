import random

def main():
    score = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        try:
            for j in range(3):
                z = int(input(f"{x[0]} + {x[1]} = "))
                if z == x[0] + x[1]:
                    score += 1
                    break
                else:
                    print("EEE")
            else:
                print(f"{x[0]} + {x[1]} = {x[0] + x[1]}")
        except ValueError:
            print("EEE")
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return (x, y)

if __name__ == "__main__":
    main()
