class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = Counter(nums)
        result = []
        for key,value in duplicates.items():
            if value > 1:
                result.append(key)
        return result
