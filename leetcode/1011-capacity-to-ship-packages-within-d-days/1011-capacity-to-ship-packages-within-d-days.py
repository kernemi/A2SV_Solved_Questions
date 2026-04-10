class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        weightMax = max(weights)
        total = sum(weights)   
        left = weightMax
        right = total
        while left < right:
            mid = (left + right) // 2
            neededDays = 1 
            cur = 0

            for x in weights:
                if cur + x > mid:
                    neededDays += 1
                    cur = 0
                cur += x

            if neededDays > days:
                left = mid + 1
            else:
                right = mid
                
        return left