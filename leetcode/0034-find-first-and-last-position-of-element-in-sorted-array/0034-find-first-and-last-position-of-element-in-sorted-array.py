class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def answer(left,right,target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        first = answer(0,len(nums)-1,target)
        last = answer(0,len(nums)-1,target + 1) -1

        if  0 <= first < len(nums) and nums[first] == target:
            return [first,last]
        return [-1,-1]
        
