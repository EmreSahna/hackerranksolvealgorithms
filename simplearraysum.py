def simpleArraySum(ar):
    i = 0
    sumArray = 0
    while ar_count != i:
        sumArray = ar[i] + sumArray
        i += 1
    print(sumArray)


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)

