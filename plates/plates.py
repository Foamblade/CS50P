def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    k = 0
    l=[]
    try:
        for i in s:
            l.append(i)
        if len(l)>=2 and len(l)<=6:
            k += 1
        try:
            if type(int(l[0]))==int and type(int(l[1]))==int:
                k += 100
            else:
                ...
        except:
            k += 5
        try:
            if int(l[2])==0:
                k += 100
        except:
            ...

    except:
        ...
    try:
        if type(int(l[-1]))==int:
            k += 1
    except:
        ...
    if '.' in l or '_' in l or ' 'in l:
        k += 1
    if k == 7 or k == 6 or k==12 or k==11:
        return True
    else:
        return False

main()
