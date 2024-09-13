def duplicates(arr):
    hashmap = dict()

    for i in arr:
        hashmap[i] = hashmap.get(i,0) + 1
    
    for x,y in hashmap.items():
        if y>1:
            return x
    return None

arr = list(map(int, input("Enter the array: ").split()))
print("Duplicate Value:",duplicates(arr))