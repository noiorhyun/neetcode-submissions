# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            # Count this node if it's good
            good = 1 if node.val >= max_so_far else 0

            # Update max for the next level
            max_so_far = max(max_so_far, node.val)

            # Recurse into left and right children
            good += dfs(node.left, max_so_far)
            good += dfs(node.right, max_so_far)

            return good

        return dfs(root, root.val)