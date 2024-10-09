def first_element_to_repeat_k_times(arr, k):
    frequency = {}
    
    for elem in arr:
        frequency[elem] = frequency.get(elem, 0) + 1
    
    for elem in arr:
        if frequency[elem] == k:
            return elem
    
    return None

arr = list(map(int, input("Enter the array: ").split()))
k = int(input(("Enter k: ")))

print("Result: ",first_element_to_repeat_k_times(arr,k))
