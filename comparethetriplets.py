def compareTriplets(a,b):
    apoint = 0
    bpoint = 0
    cpoint = 0
    i = 0
    while i != len(a):
        if a[i] < b[i]:
            bpoint += 1
        if a[i] > b[i]:
            apoint += 1
        if a[i] == b[i]:
            cpoint += 1
        i += 1
    print(apoint,bpoint)
if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a,b)
