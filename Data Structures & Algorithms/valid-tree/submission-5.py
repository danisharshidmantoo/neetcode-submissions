class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        #there should be only one component
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
        components = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                components += 1
        if components > 1:
            return False
        
        #cycle detection
        visit = set()
        def dfs_cycle(parent,node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    if dfs_cycle(node,nei):
                        return True
                elif parent != nei:
                    return True
            return False
        return not dfs_cycle(-1,0)