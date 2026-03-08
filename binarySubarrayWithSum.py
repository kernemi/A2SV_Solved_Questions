class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        sums = 0
        dicts = {0: 1}

        for x in nums:
            sums += x
            result += dicts.get(sums - goal, 0)
            dicts[sums] = dicts.get(sums, 0) + 1
            
        return result
