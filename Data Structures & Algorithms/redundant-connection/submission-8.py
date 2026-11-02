class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        father = defaultdict(int)
        for i in range(1, n + 1):
            father[i] = i
        
        def find(x):
            if father[x] == x:
                return x

            root = find(father[x])
            father[x] = root

            return root
        def isSame(x, y):

            return find(x) == find(y)

        def join(x, y):

            x = find(x)
            y = find(y)

            if x == y:
                return

            father[x] = y

        for x, y in edges:
            if isSame(x, y):
                return [x, y]
            
            join(x, y)

            

            


