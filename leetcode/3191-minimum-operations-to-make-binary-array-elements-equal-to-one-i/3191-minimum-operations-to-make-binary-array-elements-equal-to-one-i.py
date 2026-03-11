class Solution:
    def minOperations(self, nums: List[int]) -> int:
        queue = deque(nums)
        operations = 0
        
        for i in range(len(queue)-2):
            if queue[i] == 0:
                queue[i] = 1
                queue[i+1] = 1 if queue[i+1] == 0 else 0
                queue[i+2] = 1 if queue[i+2] == 0 else 0
                operations += 1
                
        if queue[-1] == 1 and queue[-2] == 1:
            return operations
        return -1