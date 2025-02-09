l = []
while True:
    try:
        name = input("Name: ")
        l.append(name)
    except EOFError:
        n = len(l)
        a = 'Adieu, adieu, to '
        if n!=1 and n!=2:
            for i in range(n):
                if i!= n-1:
                    a = a + l[i] + ', '
                else:
                    a = a + 'and ' + l[i]
        elif n==1:
            a = a + l[0]
        else:
            a = a + l[0] + ' and ' + l[1]
        print(a)
        break

