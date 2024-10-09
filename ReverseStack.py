def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)

    else:
        top = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(top)


def reverse_stack(stack):
    if not stack:
        return
    
    top_element = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top_element)

stack = list(map(int, input("Enter the array: ").split()))
print("Original Stack:", stack)

reverse_stack(stack)

print("Reversed Stack:", stack)
