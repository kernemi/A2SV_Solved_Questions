class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minn = min(len(i) for i in strs)

        while minn >= 0:
            long_com = strs[0][:minn]
            check = True

            for i in strs:
                if i[:minn] != long_com:
                    check = False
                    break   
            if check:
               return long_com
            else:
               minn -= 1
        return ""
