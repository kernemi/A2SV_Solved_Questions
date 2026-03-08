class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        dicts = defaultdict(int)
        dicts[0] = 1  
        prefixSum = 0
        result = 0
        
        for num in nums:
            prefixSum += num
            remainder = prefixSum % k
            remainder = (remainder + k) % k
            result += dicts[remainder]
            dicts[remainder] += 1
        
        return result
