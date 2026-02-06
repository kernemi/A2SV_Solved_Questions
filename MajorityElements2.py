class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = math.floor(len(nums)/3)
        freq = Counter(nums)
        result = []
        for i in freq:
            if freq[i] > x:
                result.append(i)
        return result
