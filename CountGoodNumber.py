class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odds, evens = n // 2, ceil(n / 2)
        mod = 10 ** 9 + 7

        def mypow(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            half = mypow(x, n // 2)
            if not n % 2:
                return half * half % mod
            return half * half * x % mod
        return mypow(5,evens) * mypow(4,odds)  % mod
