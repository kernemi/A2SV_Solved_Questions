class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {s[i]:i for i,ch in enumerate(s)}
       
        partitions = []
        start = 0
        end = 0
        for i, num in enumerate(s):
            end = max(end, lastIdx[num])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        return partitions
       
        
        
