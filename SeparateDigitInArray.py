class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        strings = ""
        for i in nums:
            strings += str(i)
        answer = []
        for i in strings:
            temp = int(i)
            answer.append(temp)
        return answer
        
