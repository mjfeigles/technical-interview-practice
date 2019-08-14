import sys

def main(s: str):

    s = s.replace(" ", "") # ignore spaces
    s = s.lower()
    print(s)
    ascii_const = 97

    asciiTbl = [0] *26
    print(asciiTbl)

    for i in range(len(s)):
        letter_val = ord(s[i])
        print(letter_val)
        asciiTbl[letter_val-ascii_const] += 1

    invalids = 0

    for i in range(len(asciiTbl)):
        if asciiTbl[i] % 2 != 0 and i != 0:
            invalids += 1

    if invalids > 1:
        print("False")
        return False

    print("True")
    return True


if __name__ == "__main__":
    main(sys.argv[1])