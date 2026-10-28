# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        the_node = []
        def isSame(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)

            return left and right

        def dfs(node):
            nonlocal the_node
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            if node.val == subRoot.val:
                the_node.append(node)


        dfs(root)
        if not the_node:
            return False
        else:
            flag = False
            for node in the_node:
                if isSame(node, subRoot):
                    flag = True
                    break

            return flag


        