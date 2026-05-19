class Solution:
    def climbStairs(self, n: int) -> int:
        store = defaultdict(list)
        def solve(n):
            if n == 0 or n == 1:
                return 1
            if n not in store:
                store[n] = solve(n-1) + solve(n-2)
            return store[n]
        return solve(n)
