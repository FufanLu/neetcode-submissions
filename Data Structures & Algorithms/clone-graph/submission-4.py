"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        adjanct_map = {}
        visited = set()
        visited.add(node.val)
        queue = deque([node])

        while queue:
            n = queue.popleft()
            adjanct_map[n.val] = n.neighbors
            if n.neighbors:
                for neighbor in n.neighbors:
                    if neighbor.val not in visited:
                        visited.add(neighbor.val)
                        queue.append(neighbor)


        new_node = {v : Node(v) for v in adjanct_map.keys()}

        for n, v in adjanct_map.items():
            new_node[n].neighbors = [new_node[x.val] for x in v]


        return new_node[1]
            
            




                    