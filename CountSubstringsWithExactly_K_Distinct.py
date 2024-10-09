from collections import defaultdict

def count_substrings_with_at_most_k_distinct(s,k):
    n = len(s)
    left = 0
    count = 0
    char_frequency = defaultdict(int)
    
    for right in range(n):
        char_frequency[s[right]] += 1
        
        while len(char_frequency) > k:
            char_frequency[s[left]] -= 1
            if char_frequency[s[left]] == 0:
                del char_frequency[s[left]]
            left += 1
        
        count += right - left + 1
    
    return count

def count_substrings_with_exactly_k_distinct(s, k):
    return count_substrings_with_at_most_k_distinct(s, k) - count_substrings_with_at_most_k_distinct(s, k - 1)

s = input("Enter the string: ")
k = int(input("Enter value of k: "))
print("Number of possible strings: ", count_substrings_with_exactly_k_distinct(s,k))