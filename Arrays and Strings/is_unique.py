#input: a string
#output: boolean -- true if all characters in the string are unique and false otherwise

#Run instructions:
#python3 is_unique.py str1

#Note:
# uses no additional data structures
# thus uses merge sort to alphabetically sort chars and returns false upon finding duplicate

import sys

answer = True

# a and b are lists of characters
def merge(a: [], b: []):

    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    i, j, k = 0, 0, 0 #i index of output, j index of a, k index of b
    output = [''] * (len(a) + len(b))

    while j < len(a) and k < len(b):
        if a[j] == b[k]:
            global answer
            answer = False
        if ord(a[j]) < ord(b[k]):
            output[i] = a[j]
            i, j = i+1, j+1
        else:
            output[i] = b[k]
            i, k = i+1, k+1

    while j < len(a):
        output[i] = a[j]
        i, j = i+1, j+1
    while k < len(b):
        output[i] = b[k]
        i, k = i+1, k+1

    return output


def merge_sort(a: []):
    if len(a) <= 1:
        return a

    sorted = merge(merge_sort(a[:(len(a))//2]), merge_sort(a[((len(a))//2):]))
    return sorted

if __name__ == "__main__":
    input = list(sys.argv[1])
    sorted = merge_sort(sys.argv[1])
    print(answer)

