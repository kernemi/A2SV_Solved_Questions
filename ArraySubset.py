class Solution:
    def isSubset(self, a, b):
        
        a.sort()
        b.sort()
        i = j = 0

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                return False

        return j == len(b)
