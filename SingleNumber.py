class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for i in counts:
            if counts[i] == 1:
                return i
        
