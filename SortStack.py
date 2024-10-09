def sorted_insert(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.append(temp)


def sort_stack(stack):
    if not stack:
        return
    top_element = stack.pop()

    sort_stack(stack)
    sorted_insert(stack, top_element)

stack = list(map(int, input("Enter the array: ").split()))
print("Original Stack:", stack)

sort_stack(stack)

print("Sorted Stack:", stack)