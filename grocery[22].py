def main():
    try:
        lista = {}
        r = 0
        while True:
            r += 1
            user = input().upper()
            if user not in lista:
                r = 1
                lista.update({user: r})
            else:
                lista.update({user: r})
    except EOFError:
        for number, name in sorted(lista.items()):
            print("{} {}".format(name, number))


if __name__ == "__main__":
    main()
