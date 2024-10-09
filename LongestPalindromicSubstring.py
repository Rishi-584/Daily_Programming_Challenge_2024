def longest_palindromic_substring(s):
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]
    
    if not s or len(s) == 1:
        return s
    
    longest = ""
    
    for i in range(len(s)):
        odd_palindrome = expand_from_center(i, i)
        even_palindrome = expand_from_center(i, i + 1)
        
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

s = input("Enter the string: ")
print("Result string: ", longest_palindromic_substring(s))
