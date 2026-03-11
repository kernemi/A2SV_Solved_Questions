class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and ((stack[-1].islower() and s[i].islower()) or (stack[-1].isdigit() and s[i].isdigit())):
                temp = stack.pop()
                temp = temp + s[i]
                stack.append(temp)
            elif s[i] == ']':
                ch = stack.pop()
                bracket = stack.pop()
                num = stack.pop()
                if bracket.islower() and stack[-1].isdigit():
                    w = stack.pop()
                    temp = bracket + ch
                    stack.append(int(w) * temp)
                else:
                    stack.append(int(num) * ch)
            else:
                stack.append(s[i])

        result = "".join(stack)
        return result
        