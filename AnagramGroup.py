def GroupAnagram(arr):
    res = []
    h = {}

    for i in arr:
        if i not in h:
            h[''.join(sorted(list(i)))]=[]
    
    for i in arr:
        h[''.join(sorted(list(i)))].append(i)

    for i in h.values():
        res.append(i)

    return res


            
arr = input("Enter the strings: ").split()
print("Anagram Groups: ", GroupAnagram(arr))
