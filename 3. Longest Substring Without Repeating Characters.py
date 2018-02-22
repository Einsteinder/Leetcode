#inputString = "abcabcbb"
# the answer is "abc", which the length is 3.

#inputString = "au"
# the answer is "b", with the length of 1.

inputString = "pwwkew"
# the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
		def lengthOfLongestSubstring(self, s):
			lengthList = []
			lengthList.append(1)
			if s:
				for i in range(len(s)):
					j = 0
					print("i",i)
					bank =[]
					for k in range(i,len(s)):
						print("k",k)
						print("len",len(s[i:]))
						print(k)
						print("s[k]",s[k])
						print(bank)
						if s[k] in bank:
							break
						else:
							j+=1
							print(s[k])
							bank.append(s[k])
						print(bank)
					lengthList.append(j)
				print(lengthList)
				return max(lengthList)
			else:
				return 0


so = Solution()
x = so.lengthOfLongestSubstring(inputString)
print(x)