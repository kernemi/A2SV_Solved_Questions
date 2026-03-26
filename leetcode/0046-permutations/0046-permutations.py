class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def ans(idx,temp):
            if len(temp) == len(nums):
                answer.append(temp[:])
                return
            
            for i in range(idx,len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    ans(idx,temp)
                    temp.pop()

        ans(0,[])
        return answer