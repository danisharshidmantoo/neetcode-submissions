class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def add(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows,cols = len(board),len(board[0])
        
        result,visit = set(),set()
        root = TrieNode()
        for w in words:
            root.add(w)

        def dfs(r,c,word,node):
            if (r<0 or c<0 or r==rows or c== cols or (r,c) in visit
            or board[r][c] not in node.children):
                return
            visit.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                result.add(word)
            dfs(r+1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c-1,word,node)
            visit.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,"",root)
        return list(result)
            