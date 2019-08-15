#input: two strings
#output: boolean whether one string is a permutation of the other

#Run instructions:
#python3 check_permutation.py str1 str2

#Note: does not check for special characters or numbers, converts input to lowercase

import sys

def check_permutation(str1: str, str2: str):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = list(str1)
    str2 = list(str2)
    if len(str1) != len(str2):
        print("False")
        return False
    decimal_const = 97

    tbl = [0]* 26
    for i in str1:
        tbl[ord(i)-decimal_const] += 1
    for i in str2:
        tbl[ord(i)-decimal_const] -= 1
        if tbl[ord(i)-decimal_const] < 0:
            print("False")
            return False
    print("True")
    return True



if __name__ == "__main__":
    check_permutation(sys.argv[1], sys.argv[2])