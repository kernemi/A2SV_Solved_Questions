class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsarray = list(map(str,nums))
        numsarray.sort(key= lambda x: x*10, reverse = True)
        if numsarray[0] == '0':
            return "0"
        largest = ''.join(numsarray)
        return largest
        
