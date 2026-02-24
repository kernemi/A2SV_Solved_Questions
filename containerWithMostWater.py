class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        p = 0
        q = len(height) -1
        while p < q:
            tempo = (q-p) * min(height[p],height[q])
            area = max(tempo,area)
            if height[p] >= height[q]:
                q -= 1
            else:
                p += 1
        return area
        
