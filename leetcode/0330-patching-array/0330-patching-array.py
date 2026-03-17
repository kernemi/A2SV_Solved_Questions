class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 1
        i = 0
        answer = 0
        
        while count <= n:
            if i < len(nums) and nums[i] <= count:
                count += nums[i]
                i += 1
            else:
                count += count
                answer += 1

        return answer