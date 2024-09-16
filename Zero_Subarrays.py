def ZeroSumSubarrays(arr):
    prefix_sum_map = {}
    prefix_sum = 0
    result = []
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum == 0:
            result.append((0, i))
        
        if prefix_sum in prefix_sum_map:
            for start_index in prefix_sum_map[prefix_sum]:
                result.append((start_index + 1, i))
        
        if prefix_sum in prefix_sum_map:
            prefix_sum_map[prefix_sum].append(i)
        else:
            prefix_sum_map[prefix_sum] = [i]
    
    return result


arr = list(map(int, input("Enter the array: ").split()))
print("Leaders in the array:", ZeroSumSubarrays(arr))
