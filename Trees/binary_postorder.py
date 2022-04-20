# 145. Binary Tree Postorder Traversal

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    	if root is None:
    		return []
    	return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]