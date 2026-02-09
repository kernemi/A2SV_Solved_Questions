class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        numsdict = {i:nums[i] for i in range(len(nums))}
        answer = []
        total = sum(numsdict[i] for i in numsdict if numsdict[i]%2 == 0)
        for i in range(len(queries)):
            if numsdict[queries[i][1]] % 2 == 0:
                total -= numsdict[queries[i][1]]
            numsdict[queries[i][1]] += queries[i][0]
            if numsdict[queries[i][1]]%2 == 0:
                total += numsdict[queries[i][1]]
            answer.append(total)
        if answer:
            return answer
        else:
            return [0]
