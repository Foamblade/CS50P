import sys

import inflect

from datetime import date, timedelta

def main():
    try:
        dob = date.fromisoformat(input("Date of Birth: "))
        print(convert(dob))
    except:
        sys.exit("Invalid date")
def convert(dob):
    try:
        a = ''
        p = inflect.engine()
        today = date.today()
        diff = today - dob
        minutes = int(timedelta.total_seconds(diff)/60)
        l = p.number_to_words(minutes).split()
        for i in l:
            if i == 'and':
                l.remove(i)
        for i in l:
            a = a + i + ' '

        return a.capitalize() + 'minutes'

    except:
        sys.exit("Invalid Input")

if __name__ == "__main__":
    main()
