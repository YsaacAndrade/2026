import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    x = 0
    t = 0
    for char in ip:
        if char.isalpha():
            return False
        if char == ".":
            x += 1
    if x == 3:
        ip = ip.split(".")
        for num in ip:
            if tem := re.match(r"^0.*[0-9][0-9]$", num):
                return False
            else:
                pass
            num = int(num)
            if (num > 255) or (num < 0):
                return False
            else:
                t += 1
                pass
        if t == 4:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
