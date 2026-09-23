class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
    
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix),len(matrix[0])
        rowZero,colZero = False,False
        for c in range(1,cols):
            if matrix[0][c] == 0:
                rowZero = True
        for r in range(1,rows):
            if matrix[r][0] == 0:
                colZero = True 
        if matrix[0][0] == 0:
            rowZero,colZero = True, True
       
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for c in range(1,cols):
            if matrix[0][c] == 0:
                for r in range(1,rows):
                    matrix[r][c] = 0
        for r in range(1,rows):
            if matrix[r][0] == 0:
                for c in range(1,cols):
                    matrix[r][c]  = 0
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
        if colZero:
            for r in range(rows):
                matrix[r][0] = 0
 