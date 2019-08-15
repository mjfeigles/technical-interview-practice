"""
input: a string
output: min(compressed string, original string)

Run instructions:
python3 stringCompression.py str
"""
import sys

def setZeroes(self, matrix: [[]]) -> None:

    i, j = 0, 0

    row = {}
    col = {}

    while i < len(matrix):  # row
        while j < len(matrix[i]):  # col
            print(matrix[i][j])
            if matrix[i][j] == 0:
                print("hello")
                row.add(i)
                col.add(j)
                j = len(matrix[i])  # end inner loop iteration
            j += 1
        i += 1
        j = 0


    for item in row:
        matrix[item] = [0] * len(matrix[item])

    for item in col:
        for k in range(0, len(matrix)):
            matrix[k][item] = 0

if __name__ == "__main__":
    matrix = sys.argv[1].translate(sys.argv[1].maketrans({"[":"", "]":"", " ":""})) #get rid of spaces and brackets from input

    print(matrix)
    setZeroes(matrix)