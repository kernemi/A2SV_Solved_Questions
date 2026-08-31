class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        for x in strs:
            temp = list(x)
            temp.sort()
            new = "".join(temp)
            answer.append(new)
        
        dicts = defaultdict(list)

        for x,y in enumerate(answer):
            dicts[y].append(x)

        result = []

        for x in dicts:
            new = []
            for y in dicts[x]:
                new.append(strs[y])
            result.append(new)
            
        return result