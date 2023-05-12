def main(seq):
    max_len = len(str(max(seq))) + 1
    for i, num in enumerate(seq):
        print(f"{i:>{1}} {num:>{max_len}}")


if __name__ == "__main__":
    main()