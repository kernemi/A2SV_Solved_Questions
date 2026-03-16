class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lists = [-1]
        left = []

        for idx, height in enumerate(heights):
            while lists and lists[-1] != -1 and heights[lists[-1]] >= height:
                lists.pop()
            left.append(abs(lists[-1] - len(heights) + 1))
            lists.append(idx)

        lists = [-1]
        heights.reverse()
        maxArea = 0
        for idx, height in enumerate(heights):
            while lists and lists[-1] != -1 and heights[lists[-1]] >= height:
                lists.pop()
            area = height * (left[len(heights) - idx - 1] - lists[-1] - 1)
            lists.append(idx)
            maxArea = max(maxArea, area)

        return maxArea
