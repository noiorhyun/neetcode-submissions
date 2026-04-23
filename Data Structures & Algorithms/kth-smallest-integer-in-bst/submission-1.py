# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        self._inorder(root, k)
        return self.result

    def _inorder(self, node, k):
        if not node or self.result is not None:
            return
        
        self._inorder(node.left, k)

        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        self._inorder(node.right, k)