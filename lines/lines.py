import sys

if len(sys.argv) == 2:
    if '.py' not in sys.argv[1]:
        sys.exit('Not a python file')
    else:
        try:
            n = 0
            with open(sys.argv[1],'r') as file:
                data = file.readlines()
                for i in data:
                    if len(i.strip()) > 0:
                        if '#' not in i:
                            n += 1

                print(n)
        except:
            sys.exit("File does not exist")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    sys.exit("Too few command-line arguments")
