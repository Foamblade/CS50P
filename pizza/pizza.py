import sys
import csv
from tabulate import tabulate

def get_file():
    try:
        if len(sys.argv) == 2:
            file_name = sys.argv[1]
            if file_name.endswith('.csv'):
                return file_name
            else:
                sys.exit("Not a CSV file")
        else:
            sys.exit("Too few command-line arguments")
    except:
        ...

def convert(file_name):
    try:
        with open(file_name, 'r') as file:
            data = csv.DictReader(file)
            return tabulate(data, tablefmt="grid")
    except:
        sys.exit("Invalid file")

def main():
    print(convert(get_file()))

if __name__ == "__main__":
    main()
