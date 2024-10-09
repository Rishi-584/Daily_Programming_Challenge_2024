class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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

def isSymmetric(root: TreeNode) -> bool:
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.value == t2.value) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
    
    return isMirror(root.left, root.right)

values = list(input(f"Enter the node values (space-separated): ").split())

root = build_tree(values)
print(isSymmetric(root))