while True:
    try:
        x, y = input("Fraction: ").split('/')
        try:
            value = (int(x)/int(y))*100
            if value <= 1:
                print("E")
                break
            elif value >= 99 and value <=100:
                print("F")
                break
            elif value > 1 and value < 99:
                print(round(value), '%', sep='')
                break
            else:
                ...
        except ZeroDivisionError:
            ...

    except ValueError:
        ...
