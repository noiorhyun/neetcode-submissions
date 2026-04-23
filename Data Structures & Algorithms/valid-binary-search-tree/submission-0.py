# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            # base case
            if not node:
                return True

            if not (low < node.val < high):
                return False

            left_is_valid = dfs(node.left, low, node.val)
            right_is_valid = dfs(node.right, node.val, high)

            return left_is_valid and right_is_valid

        return dfs(root, float('-inf'), float('inf'))