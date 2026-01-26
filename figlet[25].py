from pyfiglet import Figlet, FontNotFound
import sys
'''

Need pip install pyfiglet

'''
def main():
    try:
        figlet = Figlet()
        x = "-f", "--font"
        if len(sys.argv) >= 2:
            if sys.argv[1] in x:
                figlet.setFont(font=sys.argv[2])
                user = input("Input: ")
                print(figlet.renderText(user))
            else:
                sys.exit("Invalid usage")
        else:
            user = input("Input: ")
            print(figlet.renderText(user))


    except (IndexError, FontNotFound):
        sys.exit("Invalid usage")




if __name__ == "__main__":
    main()
