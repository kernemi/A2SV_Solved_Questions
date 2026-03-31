class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def solve(path, idx):
            if len(path) >= 2:
                answer.append(path[:])

            used = set() 
            
            for i in range(idx, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in used:
                    continue
                
                used.add(nums[i])
                path.append(nums[i])
                solve(path, i + 1)
                path.pop()

        answer = []
        solve([], 0)
        return answer