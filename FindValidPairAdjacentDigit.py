class Solution:
    def findValidPair(self, s: str) -> str:
        scount = Counter(s)
        result = []
        for num,freq in scount.items():
            if int(num) == freq:
                result.append(num)
        if len(result) < 2:
            return ""
        else:
            choices = []
            for i in range(len(result)):
                for j in range(len(result)):
                    if i!=j:
                        temp = f"{result[i]}{result[j]}"
                        choices.append(temp)
            for x in range(len(s)-1):
                if s[x:x+2] in choices:
                    return s[x:x+2]
            return ""
