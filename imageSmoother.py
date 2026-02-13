class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        answer = [[0 for j in row] for row in img]
        moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(len(img)):
            for j in range(len(img[0])):
                count = 0
                for x,y in moves:
                    if  0 <= i+x < len(img) and 0 <= y+j < len(img[0]):
                        answer[i][j] += img[i+x][j+y]
                        count += 1
                answer[i][j] //= count
        return answer
                
