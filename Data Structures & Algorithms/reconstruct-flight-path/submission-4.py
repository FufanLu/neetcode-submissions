class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse = True)

        for u, v in tickets:
            adj[u].append(v)

        res = []

        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            
            res.append(src)
        
        dfs('JFK')

        return res[::-1]
                
                

        
        