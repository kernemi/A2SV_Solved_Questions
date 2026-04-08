class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        dicts = list(enumerate(nums)) 

        def mergeSort(dicts):
            if len(dicts) <= 1:
                return dicts
            
            mid = len(dicts) // 2
            left = mergeSort(dicts[:mid])
            right = mergeSort(dicts[mid:])
            
            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                   
                    result[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
           
            while i < len(left):
                result[left[i][0]] += j
                merged.append(left[i])
                i += 1
            

            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged

        mergeSort(dicts)
        return result
