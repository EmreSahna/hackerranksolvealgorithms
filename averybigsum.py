def aVeryBigSum(ar):
    sumArray = 0
    i = 0
    while i != ar_count:
        sumArray = sumArray + ar[i]
        i += 1
    print(sumArray)
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)

