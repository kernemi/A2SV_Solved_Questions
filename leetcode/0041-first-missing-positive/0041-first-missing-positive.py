class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        mini = 1
        
        for i in range(len(nums)):
            if nums[i] < 1 or (i >= 1 and nums[i] == nums[i-1]):
                continue
            elif nums[i] == mini:
                mini += 1
            else:
                return mini
                
        return mini