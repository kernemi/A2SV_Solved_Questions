# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        
        while left < n:
            mid = (left + n) // 2
            
            if isBadVersion(mid):
                n = mid
            else:
                left = mid + 1
        return left