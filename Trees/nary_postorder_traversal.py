# 590. N-ary Tree Postorder Traversal

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = []
        for node in root.children:
            res.extend(self.preorder(node))
        res.append(root.val)
        
        return res