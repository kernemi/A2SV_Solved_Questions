class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums)
        temp = dict(sorted(temp.items(), key= lambda x:x[1], reverse=True))
        keys = list(temp.keys())

        if len(keys) < k:
            return keys
        return keys[:k]
            
