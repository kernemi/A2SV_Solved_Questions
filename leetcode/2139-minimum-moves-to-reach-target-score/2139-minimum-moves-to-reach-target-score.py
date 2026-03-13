class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        total = 0
        while target > 1:
            if maxDoubles == 0:
                return (target-1) + total
            elif target % 2 != 0:
                target -= 1
                total += 1
            elif target % 2 == 0:
                target //= 2
                total += 1
                maxDoubles -= 1
        return total
