class Solution:
    def isMatch(self, s, p):
        table = []
        for i in range(len(s)+1):
            tableRow =[]
            for j in range(len(p)+1):
                tableRow.append(False)
            table.append(tableRow)
        table[0][0] = True

        for j in range(1, len(p)+1):
            if p[j-1] == "*":
                table[0][j] = table[0][j-2]

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    table[i][j] = table[i-1][j-1]
                elif p[j-1] == "*":
                    table[i][j] = table[i][j-2]
                    if p[j-2] == "." or p[j-2] == s[i-1]:
                        table[i][j] = table[i-1][j] or table[i][j]
                else:
                    table[i][j] = False
        return table[len(s)][len(p)]





so = Solution()
print(so.isMatch("mississippi","mis*.is*p*."))
print(so.isMatch("aab","c*a*b"))
print(so.isMatch("ab",".*c"))
print(so.isMatch("aa","a*"))