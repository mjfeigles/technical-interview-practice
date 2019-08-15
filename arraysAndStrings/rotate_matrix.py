#input: n x n matrix as 2D array
#output: the same matrix rotated 90 degrees

#Run instructions:
#python3 rotate_matrix.py matrix1

# Example matrix1: (can include spaces or not; must be n x n)
# [[1, 2], [3, 4]]
# [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

import sys
import math

def matrixRotate(matrix):

    # convert input (string) to 2D array

    matrix = matrix.translate(matrix.maketrans({"[":"", "]":"", " ":""})) #get rid of spaces and brackets from input
    matrix = matrix.split(',')
    n =  math.sqrt(len(matrix))

    if (n - int(n) != 0):
        print("Matrix must be n x n")
        return # matrix not n x n

    n = int(n)

    mtx = [[(int(matrix[i]) + (j*n)) for i in range(n)] for j in range(n)]
    print(mtx)

    if mtx is None or len(mtx[0]) == 0:
        return

    for i in range(n//2):
        top, left = i, i
        right, bottom = n-i-1, n-i-1
        for j in range((n//(i+1))-1):
            temp = mtx[top][left + j]
            mtx[top][left + j] = mtx[bottom-j][left]
            mtx[bottom-j][left] = mtx[bottom][right-j]
            mtx[bottom][right-j] = mtx[top+j][right]
            mtx[top+j][right] = temp

    print(mtx)

if __name__ == "__main__":
    matrixRotate(sys.argv[1])


