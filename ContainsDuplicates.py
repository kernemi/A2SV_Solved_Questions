class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsset = set(nums)
        if len(nums) == len(numsset):
            return False
        else:
            return True
