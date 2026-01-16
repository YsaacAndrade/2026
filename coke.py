def main():

    coke = 50

    values = (25, 10, 5)

    while coke > 0:
        user = int(input("Insert Coin: "))

        if user in values:
            if user == 25:
                coke = coke - 25
                if coke > 0:
                    print(f"Amount due: {coke}")
                else:
                    coca = str(coke)
                    coca1 = coca.strip("-")
                    print(f"change owed: {coca1}")

            elif user == 10:
                coke = coke - 10
                if coke > 0:
                    print(f"amount due: {coke}")
                else:
                    coca = str(coke)
                    coca1 = coca.strip("-")
                    print(f"change owed: {coca1}")

            elif user == 5:
                coke = coke - 5
                if coke > 0:
                    print(f"amount due: {coke}")
                else:
                    coca = str(coke)
                    coca1 = coca.strip("-")
                    print(f"change owed: {coca1}")
        else:
            print()


if __name__ == "__main__":
    main()