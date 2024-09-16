def TrapWater(arr):
    if not arr:
        return 0
    
    left, right = 0, len(arr) - 1
    left_max, right_max = arr[left], arr[right]
    total_water = 0
    
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, arr[left])
            total_water += max(0, left_max - arr[left])
        else:
            right -= 1
            right_max = max(right_max, arr[right])
            total_water += max(0, right_max - arr[right])
    
    return total_water

arr = [2,0,2] #list(map(int, input("Enter the heights: ").split()))
print("Total Trapped Water:", TrapWater(arr))