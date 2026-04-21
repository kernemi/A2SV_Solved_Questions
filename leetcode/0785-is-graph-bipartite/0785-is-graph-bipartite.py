class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def solve(idx):
            temp = True
            for neighbor in graph[idx]:
                if color[neighbor] == -1:
                    if color[idx] == 0:
                        color[neighbor] = 1
                    else:
                        color[neighbor] = 0
                    
                    temp =  temp and solve(neighbor)

                elif color[idx] == color[neighbor]:
                    return False
            return temp

        color = [-1 for _ in range(len(graph))]
        result = True
        for i in range(len(color)):
            if color[i] == -1:
                color[i] = 0
                result = result and solve(i)
        return result

            

