from collections import deque

def sliding_window_maximum(arr, k):
    result = []
    dq = deque()
    
    for i in range(len(arr)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

arr = list(map(int, input("Enter the array: ").split()))
k = int(input(("Enter k: ")))

print("Result: ",sliding_window_maximum(arr,k))