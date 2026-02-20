class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return []

        n = len(arr)
        res = []
        for i in range(n):
            max_idx = arr.index(max(arr[0:n-i])) 
            k = max_idx + 1
            if k > 1:
                res.append(k)

            p = 0
            q = max_idx
            while p < q:
                arr[p], arr[q] = arr[q], arr[p]
                p += 1
                q -= 1
            
            arr = arr[0:n - i][::-1] + arr[n - i:]
            res.append(n - i)
        

        return res
        
