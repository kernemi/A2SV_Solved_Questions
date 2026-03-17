class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(num,exp):
            if exp == 0:
                return 1
            half = power(num,exp//2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * num
        if n < 0:
            x = 1/x
            n = -n
        return power(x,n)