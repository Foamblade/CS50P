import sys
import csv

def get_file():
    if len(sys.argv) == 3:
        if '.csv' in sys.argv[1] and '.csv' in sys.argv[2]:
            return [sys.argv[1], sys.argv[2]]
        else:
            sys.exit("Could not read csv file")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def convert(before, after):
    with open(before) as csvfile:
        data = csv.reader(csvfile)
        l = []
        for i in data:
            try:
                x = i[0].split(', ')
                l.append([x[1],x[0],i[1]])
            except:
                ...

    with open(after, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['first', 'last', 'house'])
        for i in l:
            writer.writerow(i)
    with open(after) as f:
        data = csv.reader(f)
        for i in data:
            print(i)

convert(get_file()[0], get_file()[1])

