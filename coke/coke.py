Due = 50
while True:
    insert = int(input("Insert Coin:"))
    if insert==5 or insert==10 or insert==25:
        Due -= insert
        if Due <= 0:
            print("Change Owed:", (-1)*Due)
            break
        print("Amount Due:", Due)
    else:
        print("Amount Due:", Due)

