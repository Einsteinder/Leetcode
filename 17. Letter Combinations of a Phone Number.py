class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        """
        :type digits: str
        :rtype: List[str]
        """
        self.keyMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.result = []
        def dfs(s,index,temp):
            if len(s) == len(temp):
                self.result.append("".join(x for x in temp))
                return
            for char in self.keyMap[s[index]]:
                temp.append(char)
                dfs(s,index + 1,temp)
                temp.pop()
        dfs(digits,0,[])
        return self.result
so = Solution()
print(so.letterCombinations("23"))

