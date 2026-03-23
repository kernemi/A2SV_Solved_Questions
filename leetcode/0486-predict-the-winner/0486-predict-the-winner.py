class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(nums,turn):
            if not nums:
                return 0
            if turn:
                return max((predict(nums[1:],not turn) + nums[0]),(predict(nums[:-1],not turn) + nums[-1]))

            return min((predict(nums[1:],not turn) - nums[0]),(predict(nums[:-1],not turn) - nums[-1]))
        
        return predict(nums,True) >= 0