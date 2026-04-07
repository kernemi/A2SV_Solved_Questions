class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        def solve(idx,path):
            if idx > len(nums):
                return 
            if path not in answer:
                answer.append(path[:])

            for i in range(idx,len(nums)):
                path.append(nums[i])
                solve(i+1,path)
                path.pop()
        solve(0,[])
        return answer