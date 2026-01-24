import csv
import sys
import os
from tabulate import tabulate


'''

requires pip install tabulate

'''

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    elif len(sys.argv) == 2:
        if not "." in sys.argv[1]:
            print("Not a CSV file")
        else:
            if os.path.isfile(sys.argv[1]):
                if ".csv" not in os.path.splitext(sys.argv[1]):
                    sys.exit("Not a CSV file")
                else:
                    with open(sys.argv[1]) as file:
                        x = csv.reader(file)
                        print(tabulate(x, headers="firstrow", tablefmt="grid"))
            else:
                sys.exit("File does not exist")



if __name__ == "__main__":
    main()
