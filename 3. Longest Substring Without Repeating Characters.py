#inputString = "abcabcbb"
# the answer is "abc", which the length is 3.

#inputString = "au"
# the answer is "b", with the length of 1.

inputString = "pwwkew"
# the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
	def lengthOfLongestSubstring(self, s):
		bank = {}
		pointer = 0
		maxValue = 0
		for index,value in enumerate(s):
			if value in bank:
				pointer = max(pointer,bank[value]+1)
			maxValue = max(maxValue,index-pointer+1)
			bank[value]=index

		return maxValue




so = Solution()
x = so.lengthOfLongestSubstring(inputString)
print(x)