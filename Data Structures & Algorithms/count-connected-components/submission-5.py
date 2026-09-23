class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visit = set()
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        def bfs(node):
            q = deque([node])
            visit.add(node)
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    for nei in adj[cur]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)

        components = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                components += 1
        return components