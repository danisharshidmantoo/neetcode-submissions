class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {} #True :part of current path, #False : not part of current path
        # not inserted means not visited yet
        path = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            path.append(c)
            return False
        for c in adj:
            if dfs(c):
                return ""
        path.reverse()
        return "".join(path)
