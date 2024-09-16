def ReverseString(s):
    arr = s.split()

    return ' '.join(arr[::-1])

s = input("Enter the string: ")
print("Result string: ", ReverseString(s))