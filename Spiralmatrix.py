class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart = 0
        colStart = 0
        rowEnd = len(matrix)
        colEnd = len(matrix[0])
        result = []

        while rowStart < rowEnd and colStart < colEnd:
            if rowStart < rowEnd and colStart < colEnd:
                result.extend(matrix[rowStart][colStart:colEnd])
                rowStart += 1
            else:
                break


            if rowStart < rowEnd and colStart < colEnd:
                for row in range(rowStart, rowEnd):
                    result.append(matrix[row][colEnd - 1])
                colEnd -= 1
            else:
                break


            if rowStart < rowEnd and colStart < colEnd:
                result.extend(matrix[rowEnd-1][colStart:colEnd][::-1])
                rowEnd -= 1
            else:
                break 


            if rowStart < rowEnd and colStart < colEnd:
                for row in range(rowEnd - 1, rowStart - 1, -1):
                    result.append(matrix[row][colStart])
                colStart += 1
            else:
                break
        
        return result
            
            


        

