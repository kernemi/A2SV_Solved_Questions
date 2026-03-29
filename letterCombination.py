class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dicts = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        answer = []

        if len(digits) == 0:
            return answer
    
        def lettercombo(index, path):
            if index >=len(digits):
                answer.append(path)
                return

            str1 =dicts[digits[index]]
            
            for i in str1:
                lettercombo(index+1, path + i)
        
        lettercombo(0, '')
        
        return answer
        
