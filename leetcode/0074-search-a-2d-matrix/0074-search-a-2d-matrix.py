class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = -1
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            else:
                k = i
                break
        if k == -1:
            return False
        
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left+right)//2
            if matrix[k][mid] == target:
                return True
            elif matrix[k][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False