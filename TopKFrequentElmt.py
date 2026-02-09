class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = Counter(nums)
        counting = dict(sorted(counting.items(),key=lambda x:x[1], reverse=True))
        answer = []
        for i in counting:
            answer.append(i)
        return answer[:k]
