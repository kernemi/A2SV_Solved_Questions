class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        temp = []
        queue = deque()

        for i,num in enumerate(nums):
        
            while queue and num > nums[queue[-1]]:
                queue.pop()
               
            if queue and i-k >= queue[0]:
                queue.popleft()
            
            queue.append(i) 
            temp.append(nums[queue[0]])

        return temp[k-1:]
         