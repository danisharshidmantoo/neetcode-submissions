class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        #check if there is only single component
        visit = set()
        result = 0
        def dfs(n):
            if n in visit:
                return 
            visit.add(n)
            for nei in adj[n]:
                dfs(nei)
        for i in range(n):
            if i not in visit:
                dfs(i)
                result += 1
        if result > 1:
            return False
        #check if it is acyclic
        visit = set()
        def check(parent,cur):
            if cur in visit and parent in visit:
                return False
            if cur in visit:
                return True
            visit.add(cur)
            result = True
            for nei in adj[cur]:
                if nei != parent:
                    result = result & check(cur,nei)
            return result
        return check(-1,0)
