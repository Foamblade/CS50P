from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

l = figlet.getFonts()
if len(sys.argv) == 1:
    x = input("Input: ")
    f = random.choice(l)
    figlet.setFont(font=f)
    print("Output: ", figlet.renderText(x))
elif len(sys.argv) == 3:
    if sys.argv[1]=='-f' or sys.argv[1]=='--font' and sys.argv[2] in l:
        x = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print("Output: ", figlet.renderText(x))
    else:
        sys.exit("Wrong input")
else:
    sys.exit("Wrong input")
