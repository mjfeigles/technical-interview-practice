import sys


def main(s: str, l: int):
    chars = list(s)
    print(chars)
    l = int(l)

    spaceCount = 0

    for i in range(l):
        if chars[i] == ' ':
            spaceCount += 1

    index = l + (spaceCount * 2)
    print(index)

    if l < len(chars): #set null char to terminate string
        chars[l] = '\0'

    for i in range(l-1, -1, -1):
        if chars[i] == ' ':
            chars[index-1] = '0'
            chars[index-2] = '2'
            chars[index-3] = '%'
            index -= 3
        else:
            chars[index-1] = chars[i]
            index -= 1
    print(chars)






if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])