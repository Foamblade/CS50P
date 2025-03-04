import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers = ip.split('.')
        for i in numbers:
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    else:
        return False




if __name__ == "__main__":
    main()
