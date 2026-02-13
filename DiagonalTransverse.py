class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dicts = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dicts[i+j].append(mat[i][j])
        result = []
        for key,value in dicts.items():
            if key % 2 == 0:
                value.reverse()
            result.extend(i for i in value)
        return result

        
