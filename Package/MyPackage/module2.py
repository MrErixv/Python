def main(n):
    licznik = int(n)
    A = []
    numer = 0
    while numer < int(n):
        A.append(licznik)
        licznik += 2
        numer += 1
    return A

if __name__ == "__main__":
    main()