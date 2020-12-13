def plusMinus(arr):
    a = n
    i = 0
    ncount,pcount,zcount = 0,0,0
    while i != a:
        if arr[i] < 0 and arr[i] != 0:
            ncount += 1
        if arr[i] > 0 and arr[i] != 0:
            pcount += 1
        if arr[i] == 0:
            zcount += 1
        i += 1
    nproc = ncount / a
    pproc = pcount / a
    zproc = zcount / a
    print(pproc)
    print(nproc)
    print(zproc)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
