class Solution:
    def hIndex(self, citations: List[int]) -> int:
        k = len(citations)
       
        left = 0
        right = k - 1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] == k - mid:
                return k - mid
            elif citations[mid] < k - mid:
                left = mid + 1
            else:
                right = mid - 1

        return k - left