class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for x in counts:
            if counts[x] > 1:
                return x