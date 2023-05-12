def m5(seq):
    max_len = len(str(max(seq))) + 2
    for i, num in enumerate(seq):
        print(f"{i:>{1}}{num:>{max_len}}")


if __name__ == "__main__":
    m5()