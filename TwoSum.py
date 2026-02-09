class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumdict = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in sumdict and sumdict[num2] != i:
                return [i,sumdict[num2]]
        else:
            return []
      
