def main(lista):
    licz_20 = 0
    licz_7 = 0
    for x in lista:
        if x == 20:
            licz_20 += 1
        elif x == 7:
            licz_7 += 1
    if licz_20 == 2 and licz_7 >= 3:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()