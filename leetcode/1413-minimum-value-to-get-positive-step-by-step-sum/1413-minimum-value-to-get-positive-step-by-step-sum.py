class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minprefix = float("inf")
        total = 0
        for i in nums:
            total += i
            minprefix = min(minprefix,total)
        return max(1,1-minprefix)
        