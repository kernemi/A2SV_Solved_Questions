class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxdeque = deque()
        mindeque = deque()
        left = 0
        result = 0

        for right in range(len(nums)):            
            while maxdeque and nums[right] > maxdeque[-1]:
                maxdeque.pop()
            maxdeque.append(nums[right])
            while mindeque and nums[right] < mindeque[-1]:
                mindeque.pop()
            mindeque.append(nums[right])
            while maxdeque[0] - mindeque[0] > limit:
                if nums[left] == maxdeque[0]:
                    maxdeque.popleft()
                if nums[left] == mindeque[0]:
                    mindeque.popleft()
                left += 1
            result = max(result, right - left + 1)
        return result
