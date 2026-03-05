class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dicts = {0: -1}
        sums = 0

        for i in range(len(nums)):
            sums += nums[i]
            remainder = sums % k

            if remainder in dicts:
                if i - dicts[remainder] >= 2:
                    return True
            else:
                dicts[remainder] = i

        return False
