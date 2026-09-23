class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom=0, len(matrix)-1
        while top<=bottom:
            row=(top+bottom)//2
            if matrix[row][-1]<target:
                top=row+1
            elif matrix[row][0]>target:
                bottom=row-1
            else:
                break
        if not top<=bottom:
            return False
        l, r=0, len(matrix[row])-1
        while l<=r:
            mid=l+(r-l)//2
            if target==matrix[row][mid]:
                return True
            elif target>matrix[row][mid]:
                l=mid+1
            else:
                r=mid-1
        return False
            