class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = (len(nums)* (len(nums) +1))//2
        needed = n - sum(nums)

        for i in range(1,len(nums)+1):
            if i not in nums:
                return [i- needed , i]