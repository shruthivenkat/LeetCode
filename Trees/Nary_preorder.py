# 589. N-ary Tree Preorder Traversal

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res