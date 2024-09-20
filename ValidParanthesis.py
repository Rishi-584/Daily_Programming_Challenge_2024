def ValidParenthesis(s):
    bracket = {'(':')', '{':'}', '[':']'}
    stack = []

    if len(s)%2==1:
        return False

    for i in s:
        if i in bracket:
            stack.append(i)
        elif i not in bracket and bracket[stack[-1]]==i:
            stack.pop()
    return len(stack)==0

s = input("Enter the string: ")
print(ValidParenthesis(s))