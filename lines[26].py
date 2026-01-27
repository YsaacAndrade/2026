import sys
import os
def main():
    try:
        less = 0
        if len(sys.argv) == 2:
            if "." not in sys.argv[1]:
                sys.exit("Not a Python file")
            else:
                if os.path.isfile(sys.argv[1]):
                    if ".py" not in os.path.splitext(sys.argv[1]):
                        sys.exit("Not a Python file")
                    else:
                        with open(sys.argv[1]) as file:
                            lines = file.readlines()
                            total_lines = len(lines)
                            for item in lines:
                                if item.lstrip().startswith("#"):
                                    less += 1
                                if item.rstrip() == "":
                                    less += 1
                            print(total_lines - less)
                else:
                    sys.exit("File does not exist")

        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    except (FileExistsError, FileNotFoundError):
            sys.exit("File does not exist")
if __name__ == "__main__":
    main()
