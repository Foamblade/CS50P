camelCase=input("camelCase: ")

def snake_case(camelCase):
    a = ''
    for i in camelCase:
        if i.isupper():
            a = a + "_" + i.lower()
        else:
            a = a + i

    print("snake_case: ", a)

snake_case(camelCase)
