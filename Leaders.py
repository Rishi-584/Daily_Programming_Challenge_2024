def Leader(arr):
    if arr==sorted(arr,reverse=True):
        return arr
    elif arr==sorted(arr):
        return [arr[-1]]
    
    n = len(arr)
    res=[]
    for i in range(n):
        if len(arr[i+1:])>0 and arr[i]>max(arr[i+1:]):
            res.append(arr[i])
    res.append(arr[-1])
    return res

arr = list(map(int, input("Enter the array: ").split()))
print("Leaders in the array:",Leader(arr))