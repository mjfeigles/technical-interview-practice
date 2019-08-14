#input: two strings
#output: boolean if those strings can be made the same by adding, removing, or changing a character

#Run instructions:
#python3 oneAway.py str1 str2

import sys


def main(A: str, B: str):
    if abs(len(A) - len(B)) > 1:
        print("False")
        return False
    differences = 0
    dict = {}
    for i in range(len(A)):
        if A[i] not in dict:
            dict[A[i]] = 1
        else:
            dict[A[i]] = dict[A[i]] + 1

    for i in range(len(B)):
        if B[i] not in dict:
            differences += 1
        else:
            dict[B[i]] = dict[B[i]] - 1
            if dict[B[i]] < 0:
                differences += 1
    if differences > 1:
        print("False")
        return False
    print("True")
    return True




if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

