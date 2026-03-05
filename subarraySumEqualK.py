class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        prefix = {0:1}

        for x in nums:
            sums += x

            if sums - k in prefix:
                count += prefix[sums - k]

            prefix[sums] = prefix.get(sums,0) + 1

        return count 
