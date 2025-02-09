def main():
    time = input("What time is it? ")
    if convert(time)>=7 and convert(time)<=8:
        print("breakfast time")
    elif convert(time)>=12 and convert(time)<=13:
        print("lunch time")
    elif convert(time)>=18 and convert(time)<=19:
        print("dinner time")
    else:
        print("")


def convert(time):
    l = time.split(":")
    x = float(l[0]) + float(l[-1])/60
    return x


if __name__ == "__main__":
    main()
