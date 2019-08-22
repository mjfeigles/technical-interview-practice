import sys

def equilibriumIndex(a):
    print("hello")
    print(a)
    sumLeft = 0
    sumRight = 0
    for i in a:
        sumRight += i

    if sumRight == sumLeft:
        return 0
    i = 0
    for i in range(1, len(a)):
        sumLeft += a[i-1]
        sumRight -= a[i]
        if sumRight == sumLeft:
            print("success!")
            return i
    print("no such value")
    return -1


if __name__ == "__main__":
    print(sys.argv[1])
    inputt = [int(i) for i in sys.argv[1].split(',')]
    print("length: " + str(len(inputt)))
    answer = equilibriumIndex(inputt)
    print("answer: " + str(answer))
