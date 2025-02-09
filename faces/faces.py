
def convert(a):
    b = a.replace(':)',"🙂")
    c = b.replace(':(',"🙁")
    print(c)

def main():
    a=input()
    convert(a)

if __name__=="__main__":
    main()

