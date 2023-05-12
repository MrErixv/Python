def m3(string):
    slowa = []
    znaki = []
    z = [" ", ",", "."]
    word = ""
    for char in string:
        if char in z:
            znaki.append(char)
            if(word != ""):
                slowa.append(word)
            word = ""
        else:
            word += char
    if word != "":
        slowa.append(word)
    return slowa, znaki

if __name__ == "__main__":
    m3()