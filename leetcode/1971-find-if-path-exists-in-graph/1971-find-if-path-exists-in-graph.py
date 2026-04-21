class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def solve(node,visited):
            if node == destination:
                return True

            visited.add(node)
            for x in graph[node]:
                if x not in visited:
                    found = solve(x,visited)

                    if found:
                        return True
            return False
        
        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()

        return solve(source,visited)