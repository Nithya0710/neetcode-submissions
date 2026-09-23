class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols=len(matrix), len(matrix[0])
        if target<matrix[0][0] or target>matrix[rows-1][cols-1]:
            return False
        i=0
        while i<rows and target>=matrix[i][0]:
            i+=1
        for j in range(cols):
            if target==matrix[i-1][j]:
                return True
        return False