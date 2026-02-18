class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numssorted = sorted(nums)
        numsdict = {}
        for i in range(len(nums)):
            if numssorted[i] not in numsdict:
                numsdict[numssorted[i]] = i
        result = []
        for i in nums:
            result.append(numsdict[i])
        return result


