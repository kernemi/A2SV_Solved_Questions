class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        solution = {indices[i]:s[i] for i in range(len(s))}
        solution = dict(sorted(solution.items(),key=lambda x: x[0]))
        answer = []
        for i in solution:
            answer.append(solution[i])
        return "".join(answer)
