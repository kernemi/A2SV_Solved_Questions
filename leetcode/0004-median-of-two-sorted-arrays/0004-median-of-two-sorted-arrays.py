class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        
        result.extend(nums1[i:])
        result.extend(nums2[j:])
        
        n = len(result)
        if n % 2:
            return result[n // 2]
        else:
            return (result[n//2 - 1] + result[n//2]) / 2