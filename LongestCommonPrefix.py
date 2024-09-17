def LongestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

strs = input("Enter the strings: ").split()
print("Longest common prefix of the given strings: ", LongestCommonPrefix(strs))