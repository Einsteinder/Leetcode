class Solution:
	def longestPalindrome(self, s):
		result = {}
		for i in range(len(s)):
			for j in range(i,len(s)):
				if self.checkPalindromic(s[i:j+1]):
					result[s[i:j+1]]=j-i
		print(result)
		result = max(result.items(),key = lambda x:x[1])
		return result[0]

	def checkPalindromic(self,inputString):
		resultStr = ""
		if resultStr.join(reversed(inputString))==inputString:
			return True
		else:
			return False
so = Solution()
print(so.longestPalindrome("babad"))