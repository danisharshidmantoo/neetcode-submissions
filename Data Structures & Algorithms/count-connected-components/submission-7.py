class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        result = 0
        def dfs(n):
            if  n in visit:
                return 
            visit.add(n)
            for nei in adj[n]:
                dfs(nei)
        for i in range(n):
            if i not in visit:
                dfs(i)
                result += 1
        return result