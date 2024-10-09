def evaluate_postfix(expression):
    stack = []
    
    def apply_operator(op, b, a):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return int(a / b)
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(char, b, a)
            stack.append(result)
    
    return stack[0]

s = input("Enter the postfix expression: ")
print("Result:", evaluate_postfix(s))