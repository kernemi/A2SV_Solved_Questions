class Solution(object):
    def fib(self, n):
        answer = defaultdict(int)
        def solve(n):
            if n == 0 or n == 1:
                return n
            if n not in answer:
                answer[n] = solve(n-1) + solve(n-2)
            return answer[n]

        return solve(n)  