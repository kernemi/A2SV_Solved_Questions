class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        noZero = 0
        left = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                noZero += 1
            while noZero > 1:
                if nums[left]== 0:
                    noZero -= 1
                left += 1
            result = max(result,right-left)
        return result
