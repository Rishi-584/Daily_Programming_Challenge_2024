class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right

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
p_val = int(input("Enter the value of node p: "))
q_val = int(input("Enter the value of node q: "))

root = build_tree(values)


p_node = find_node(root, p_val)
q_node = find_node(root, q_val)
lca_node = lowest_common_ancestor(root, p_node, q_node)


if lca_node:
    print(f"The lowest common ancestor of {p_val} and {q_val} is: {lca_node.val}")
else:
    print("Lowest common ancestor not found.")
