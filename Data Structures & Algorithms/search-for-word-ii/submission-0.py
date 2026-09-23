class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def insert(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #build trie ds from the words and then dfs from each cell to find matches in 
        # the trie structure, then add the current cell to visited
        Root = TrieNode()
        Rows,Cols = len(board),len(board[0])
        for w in words:
            Root.insert(w)
        Result,visit = set(),set()
        def dfs(r,c,node,word):
            if (r<0 or c<0 or r==Rows or c==Cols or board[r][c] not in node.children or (r,c) in visit):
                return 
            word += board[r][c]
            visit.add((r,c))
            node = node.children[board[r][c]]
            if node.endOfWord:
                Result.add(word)
           
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(Rows):
            for c in range(Cols):
                dfs(r,c,Root,"")
        return list(Result)
