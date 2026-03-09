class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        nextgreatest = {}
        for num in nums2:
            while stack and stack[-1] <num:
                nextgreatest[stack.pop()] = num
            stack.append(num)
        for i in stack:
            nextgreatest[i] = -1
        return [nextgreatest[x] for x in nums1]