class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
    
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)