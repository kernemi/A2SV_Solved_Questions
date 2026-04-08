class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        leftrem = 0
        rightrem = 0
        answer = set()

        for c in s:
            if c == "(":
                leftrem += 1
            elif c == ")":
                if leftrem == 0:
                    rightrem += 1
                else:
                    leftrem -= 1
        def solve(idx,rightcount,leftcount,path,leftrem,rightrem):
            if idx == len(s):
                if leftrem == 0 and rightrem == 0:
                    answer.add(path)
                return
                
            ch = s[idx]

            if ch == "(" and leftrem > 0:
                solve(idx + 1,rightcount,leftcount,path,leftrem-1,rightrem)
            elif ch == ")" and rightrem > 0:
                solve(idx + 1,rightcount,leftcount,path,leftrem,rightrem-1)
            
            if ch not in ["(",")"]:
                solve(idx + 1, rightcount,leftcount, path + ch, leftrem, rightrem)
            elif ch == "(":
                solve(idx + 1,rightcount,leftcount + 1,path + ch,leftrem,rightrem)
            elif ch == ")":
                if rightcount < leftcount:
                    solve(idx + 1,rightcount + 1,leftcount ,path + ch,leftrem,rightrem)

        solve(0,0,0,"",leftrem,rightrem)
        return list(answer)