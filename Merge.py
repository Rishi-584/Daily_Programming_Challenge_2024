def merge(arr1,arr2):
    assert len(arr1)==len(arr2)

    n = len(arr1)
    i,j = n-1,0

    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        
        i -= 1
        j += 1
    arr1.sort()
    arr2.sort()

arr1 = list(map(int, input("Enter the array1: ").split()))
arr2 = list(map(int, input("Enter the array2: ").split()))
merge(arr1,arr2)
print("Merged arrays:", arr1,arr2)