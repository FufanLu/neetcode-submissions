class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        visited = set()

        adjacent_list = defaultdict(list)

        def dfs(curr, target):
            if curr in visited:
                return False
            
            if curr == target:
                return True

            visited.add(curr)

            for nex in adjacent_list[curr]:
                if nex not in visited:
                    if dfs(nex, target):
                        return True
            
            return False

        
        for x, y in edges:
            visited.clear()
            if dfs(x, y):
                return [x, y]

            adjacent_list[x].append(y)
            adjacent_list[y].append(x)








