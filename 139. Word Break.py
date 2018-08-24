class Solution(object):
    def wordBreak(self, s, wordDict):
        boolList = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i:i +len(word)] and (boolList[i-1] or i==0 ):
                    boolList[i+len(word)-1] = True
        print(boolList)
        return boolList[-1]
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

s = "leetcode"
wordDict = ["leet", "code"]
so = Solution()
print(so.wordBreak(s,wordDict))
