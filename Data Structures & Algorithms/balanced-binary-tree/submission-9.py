# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        max_differ = 0

        def dfs(node):
            nonlocal max_differ
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            max_differ = max(abs(left - right), max_differ)

            return max(left, right) + 1

        dfs(root)

        return max_differ <= 1

            


        