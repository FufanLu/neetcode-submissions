# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def isSame(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)

            return left and right and p.val == q.val

        def dfs(node1, node2):
            if not node1:
                return False

            if isSame(node1, node2):
                return True

            return dfs(node1.left, node2) or dfs(node1.right, node2)

        return dfs(root, subRoot)


            