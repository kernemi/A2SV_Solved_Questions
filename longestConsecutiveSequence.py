class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        maximum = 1
        count = 1
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                count = 1
            maximum = max(maximum,count)
        return maximum

