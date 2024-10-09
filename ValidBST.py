class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

def build_tree(nodes):
    nodes = [int(i) for i in nodes if i!="None"]

    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while i < len(nodes):
        current = queue.pop(0)
        
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    
    left = find_node(root.left, val)
    if left:
        return left
    
    return find_node(root.right, val)

values = list(input(f"Enter the node values (space-separated): ").split())

root = build_tree(values)

if is_valid_bst(root):
    print("This is a valid Binary Search Tree.")
else:
    print("This is not a valid Binary Search Tree.")