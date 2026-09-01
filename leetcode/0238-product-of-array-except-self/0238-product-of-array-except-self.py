class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        right = []
        answer = []

        i = 0
        j = len(nums) - 1

        while i < len(nums) and j >= 0:

            if not left and not right:
                left.append(nums[i]) 
                right.append(nums[j])
            else:
                left.append(left[-1]*nums[i])
                right.append(right[-1]*nums[j])

            i += 1
            j -= 1

        right = right[::-1]

        for i in range(len(nums)):
            if i == 0:
                answer.append(right[i+1])
            elif i == len(nums)-1:
                answer.append(left[i-1])
            else:
                answer.append(left[i-1] * right[i+1])
        
        return answer