class Solution:
	def longestPalindrome(self, s):
		w = h = len(s)
		matrix = [[False for x in range(w)] for y in range(h)] 
		for i in range(len(s)):
			matrix[i][i]=True
			try:
				if s[i] == s[i+1]:
					matrix[i][i+1]=True
			except:
				continue
		maxLenth = 0
		for i in range(len(s)):
			for j in range(len(s)):
				if s[i] == s[j] :
					m=i
					n=j
					while m<n:
						if s[m+1]==s[n-1]:
							m = m+1
							n = n-1
						else:
							break
				maxLenth = max(maxLenth,n-m)
		return maxLenth


		print(matrix)



	def checkPalindromic(self,inputString):
		resultStr = ""
		if resultStr.join(reversed(inputString))==inputString:
			return True
		else:
			return False
so = Solution()
print(so.longestPalindrome("cbbd"))