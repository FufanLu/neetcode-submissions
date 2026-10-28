# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []

        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                res.append('N')
                continue

            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        return ' '.join(map(str, res))



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None

        vals = list(data.split())
        queue = deque()
        node = TreeNode(int(vals[0]))
        queue.append(node)
        i = 1

        while queue and i < len(vals):
            n = queue.popleft()
            if vals[i] == 'N':
                n.left = None
            else:
                n.left = TreeNode(int(vals[i]))
                queue.append(n.left)

            i += 1

            if vals[i] == 'N':
                n.right = None
            else:
                n.right = TreeNode(int(vals[i]))
                queue.append(n.right)

            i += 1
        
        return node




