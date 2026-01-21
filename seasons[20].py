import inflect
import datetime
import re
import sys

def minutes(s):
    p = inflect.engine()
    if x := re.search(f"([0-2][0-9][0-9][0-9])-(1[0-2]|0[0-9])-(0[0-9]|1[0-9]|2[0-9]|3[0-1])", s):
        y, m, d = x.group(1,2,3)
        data = int(y), int(m), int(d)
        z = datetime.date.today().strftime("%Y %m %d")
        c = [int(z[0:4]), int(z[5:7]), int(z[8:10])]
        d2 = datetime.datetime(data[0], data[1], data[2])
        d1 = datetime.datetime(c[0], c[1], c[2])
        calc = d1 - d2
        ue = calc * 24 * 60
        p = f"{p.number_to_words(ue.days, andword='')} minutes".capitalize()
        return p
    else:
        sys.exit("Invalid date")

def main():
    user = input("Date of Birth: ")
    print(minutes(user))

if __name__ == "__main__":
    main()
