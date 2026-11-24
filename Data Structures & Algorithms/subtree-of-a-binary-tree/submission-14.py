# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        target = []

        def dfs(node):
            if not node:
                return

            if node.val == subRoot.val:
                target.append(node)

            dfs(node.left)
            dfs(node.right)

        def isSame(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)

            return p.val == q.val and left and right

        dfs(root)

        for n in target:
            if isSame(n, subRoot):
                return True

        return False

                