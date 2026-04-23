# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
         
        def helper(node):
            if not node:
                return 0, True  # height, is_balanced

            left_height, left_balanced = helper(node.left)
            right_height, right_balanced = helper(node.right)

            # check current node balance
            current_balanced = abs(left_height - right_height) <= 1

            # combine
            is_balanced = left_balanced and right_balanced and current_balanced
            height = max(left_height, right_height) + 1

            return height, is_balanced

        return helper(root)[1]
