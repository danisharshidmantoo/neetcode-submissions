class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        visit = set()
        def helper(i,r,c):
            if r>= rows or c>= cols or r<0 or c<0 or (r,c) in visit or board[r][c]!=word[i]:
                return False
            if i == len(word)-1:
                if board[r][c] == word[i]:
                    return True
                return False

            visit.add((r,c))
            found = False
            if board[r][c] == word[i]: 
                found =  helper(i+1,r+1,c) or helper(i+1,r,c+1) or helper(i+1,r-1,c) or helper(i+1,r,c-1)
            visit.remove((r,c))
            return found
        result = False
        for r in range(rows):
            for c in range(cols):
                if helper(0,r,c):
                    return True
        return result