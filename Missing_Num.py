def missingnum(arr):
    k = sum(arr)
    p = arr[-1]
    s = p*(p+1)//2

    n = s-k
    if n==0:
        return p+1
    else:
        return n
arr = list(map(int, input("Enter the array: ").split()))
print("Missing number:",missingnum(arr))