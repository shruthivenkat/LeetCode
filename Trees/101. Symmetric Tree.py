# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirroring(tree1, tree2):
            if not tree1 and not tree2:
                return True
            elif not tree1:
                return False
            elif not tree2:
                return False
            elif tree1 and tree2:
                if tree1.val == tree2.val:
                    return (mirroring(tree1.left, tree2.right) and mirroring(tree1.right, tree2.left))
            
        if root is None:
            return True
        return mirroring(root, root)
        
            