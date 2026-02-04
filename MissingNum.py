class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = int((len(nums)* (len(nums)+1))/2)
        actual = sum(nums)
        return expected-actual
       
        
