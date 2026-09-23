class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        #check if there is a single component
        visit = set()
        def dfs(n):
            if n in visit:
                return
            visit.add(n)
            for nei in adj[n]:
                if nei not in visit:
                    dfs(nei)
        components = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                components += 1
        if components > 1:
            return False
        #Check for Cycle
        visit = set()
        result = True
        def dfs2(cur,parent):
            nonlocal result;
            # if cur in visit and nei!=parent :
            #     return False
            visit.add(cur)
            for nei in adj[cur]:
                if nei not in visit :
                    dfs2(nei,cur)
                    
                elif nei in visit and nei != parent:
                    result = False
                    return False

                   
        dfs2(0,-1)
        return result