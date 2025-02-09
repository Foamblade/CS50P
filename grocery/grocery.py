d={}
count = 1
while True:
    try:
        item = input()
        if item in d.keys():
            d[item] = count + 1
        else:
            d[item] = count
    except EOFError:
        for i in sorted(d.keys()):
            print(d[i], i.upper(), sep=' ')
        break
