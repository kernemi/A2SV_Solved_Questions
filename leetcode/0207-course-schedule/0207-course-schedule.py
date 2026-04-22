class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def solve(node):
            if color[node] == gray:
                return False
            if color[node] == black:
                return True
            
            color[node] = gray

            for nei in graph[node]:
                if not solve(nei):
                    return False
            
            color[node] = black
            return True
        
        white = 1
        gray = 2
        black = 3
        color = [white] * numCourses
        graph = {i:[] for i in range(numCourses)}


        for a,b in prerequisites:
            graph[b].append(a)
        

        for i in range(numCourses):
            if not solve(i):
                return False

        return True
        
            
        
        