class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        check = float('-inf')

        for num in nums[::-1]:
            if num < check:
                return True
            while stack and num > stack[-1]:
                check = stack.pop()
            stack.append(num)

        return False


