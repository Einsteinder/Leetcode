class Solution:
    def longestCommonPrefix(self, strs):
        flag = True
        j = 0
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]

        while flag and j<len(min(strs,key=lambda x:len(x))):
            first = strs[0][j]
            for i in range(0,len(strs)):
                if strs[i][j]!= first:
                    flag = False
                    return strs[0][0:j]

            j += 1
        return strs[0][0:j]

        """
        :type strs: List[str]
        :rtype: str
        """
so = Solution()
print(so.longestCommonPrefix(["a","a","a"]))