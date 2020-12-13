def diagonalDifference(arr):
    i,d,a = 0,0,0
    c = n - 1
    e = n
    sumArray1,sumArray2,sumArrayAll = 0,0,0
    while i != n:
        sumArray1 = sumArray1 + arr[i][i]
        i += 1
    while e != d:
        sumArray2 = sumArray2 + arr[a][c]
        a += 1
        c -= 1
        e -= 1
    sumArrayAll = sumArray1 - sumArray2
    if sumArrayAll < 0:
        sumArrayAll = sumArrayAll - (2*sumArrayAll)
        print(sumArrayAll)
    else:
        print(sumArrayAll)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)

