class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def ans(idx,temp):
            answer.append(temp[:])
    
            for i in range(idx,len(nums)):
                temp.append(nums[i])
                ans(i+1,temp)
                temp.pop()

        ans(0,[])
        return answer
