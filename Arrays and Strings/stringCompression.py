#input: a string
#output: min(compressed string, original string)

#Run instructions:
#python3 stringCompression.py str

import sys

def main(A: str):
    if len(A) <= 1:
        return A

    i, count, output = 0, 1, ""

    while i < len(A):
        char = A[i]
        while (i < (len(A) -1)) and (A[i] == A[i+1]):
            count += 1
            i += 1
        output = output + char + str(count)
        count = 1
        i += 1

    if len(output) > len(A):
        print(A)
        return A

    print(output)
    return output




if __name__ == "__main__":
    main(sys.argv[1])