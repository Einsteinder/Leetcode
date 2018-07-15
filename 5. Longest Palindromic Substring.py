class Solution:
	def longestPalindrome(self, s):
		table = []
		maxLength = 1
		result = s[0]
		for i in range(len(s)):
			tableRow = []
			for j in range(len(s)):
				if i == j:
					tableRow.append(1)
				else:
					tableRow.append(0)
			table.append(tableRow)
		for i in range(len(s)-1):
			if s[i] == s[i+1]:
				maxLength = 2
				result = s[i:i+2]
				table[i][i+1] = 1
		k = 3
		while k <= len(s):
			i = 0
			while i < len(s) - k + 1:
				if s[i] == s[i + k - 1] and table[i+1][i+k-2]:
					table[i][i+k-1]=1
					if k > maxLength:
						maxLength = k
						result = s[i:i+k]

				i += 1
			k += 1

		return result







so = Solution()
print(so.longestPalindrome("abcba"))