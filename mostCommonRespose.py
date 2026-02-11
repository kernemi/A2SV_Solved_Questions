class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        result = []
        for i in range(len(responses)):
            tempo = set(responses[i])
            for i in tempo:
                result.append(i)
        result.sort()
        mostCommon = Counter(result)
        mostCommon = sorted(mostCommon.items(), key = lambda x: x[1] , reverse = True)
        for key in mostCommon:
            return key[0]
