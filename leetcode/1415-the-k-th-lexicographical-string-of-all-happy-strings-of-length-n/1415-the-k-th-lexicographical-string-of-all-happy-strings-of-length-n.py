class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        sample = ['a','b','c']

        def solve(path):
            if len(result) == k:
                return

            if len(path) == n:
                result.append(path[:])
                return 
            
            for x in sample:
                if (not path) or (path and path[-1] != x):
                    path.append(x)
                    solve(path)
                    path.pop()

        solve([])
       
        if len(result) < k:
            return ""
        ans = "".join(result[-1])
        return ans