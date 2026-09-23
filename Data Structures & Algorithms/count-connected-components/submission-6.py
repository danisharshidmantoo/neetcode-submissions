class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(n):
            if n in visit:
                return 
            visit.add(n)
            for nei in adj[n]:
                dfs(nei)
            return 

        for i in range(n):
            if i not in visit:
                dfs(i)
                components += 1
        return components
            
