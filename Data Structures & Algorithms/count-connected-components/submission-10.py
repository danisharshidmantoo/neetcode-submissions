class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        components = 0
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
            
        for i in range(n):
            if i not in visit:
                dfs(i)
                components += 1
        return components 


