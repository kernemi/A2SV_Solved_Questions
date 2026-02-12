class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        numsdicts = sorted(Counter(nums).items(), key = lambda x: x[1], reverse=True)
        domnums,domfreq = numsdicts[0]

        count = 0

        for i in range(len(nums)):
            if nums[i] == domnums:
                count += 1
            if count > (i+1)//2:
                right = domfreq - count
                if right > (len(nums)-1-i)//2:
                    return i
                else:
                    return -1
