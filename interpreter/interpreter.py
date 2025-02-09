exp = input('Expression: ')
x, y, z = exp.split(" ")

if y == '+':
    print(float(x)+float(z))

if y == '-':
    print(float(x)-float(z))

if y == '*':
    print(float(x)*float(z))

if y == '/':
    if z==0:
        print("Invalid input")
    else:
        print(float(x)/float(z))
else:
    print("Invalid input")
