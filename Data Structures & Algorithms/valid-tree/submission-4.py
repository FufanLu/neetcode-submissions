class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True

        adjacent_list = defaultdict(list)
        for x, y in edges:
            adjacent_list[x].append(y)
            adjacent_list[y].append(x)


        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for son in adjacent_list[i]:
                if son == prev:
                    continue
                else:
                    if not dfs(son, i):
                        return False

            return True

        return dfs(0, -1) and len(visited) == n
                

                   