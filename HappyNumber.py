class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            sums = 0
            while n > 0:
                temp= n % 10
                sums += temp ** 2
                n = n//10
            n = sums
        return True
