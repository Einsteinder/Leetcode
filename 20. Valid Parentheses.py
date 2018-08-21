class Solution:
    def isValid(self, s):
        i = 0
        relation = {"}":"{",
                    "]":"[",
                    ")":"("}
        status = []
        while i < len(s):
            if s[i] in "{[(":
                status.append(s[i])
            if s[i] in "}])":
                if len(status)>0 and relation[s[i]] == status[-1]:
                    status.pop()
                else:
                    return False
            i += 1
        if len(status)==0:
            return True
        else:
            return False



        """
        :type s: str
        :rtype: bool
        """
so = Solution()
print(so.isValid("}"))