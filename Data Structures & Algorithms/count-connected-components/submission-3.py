class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacent_list = defaultdict(list)

        for x, y in edges:
            adjacent_list[x].append(y)
            adjacent_list[y].append(x)
        
        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return

            visited.add(curr)
            for child in adjacent_list[curr]:
                if child != prev:
                    dfs(child, curr)

        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, -1)

        return count


        