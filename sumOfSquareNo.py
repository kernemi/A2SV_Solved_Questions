class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        p = 0
        q = int(math.sqrt(c))
        while p <= q:
            if p*p + q*q == c:
                return True
            elif p*p + q*q > c:
                q -= 1
            else:
                p += 1
        return False
        
