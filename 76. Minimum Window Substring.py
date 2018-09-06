#S = "cabwefgewcwaefgcf"
#T = "cae"
#S = "a"
#T = "a"
#S="ask_not_what_your_country_can_do_for_you_ask_what_you_can_do_for_your_country"
#T="ask_country"
import collections
import sys
S = "ADOBECODEBANC"
T = "ABC"
class Solution(object):
	def minWindow(self, string, target):
		target_dic = collections.Counter(target)
		r = 0
		l = 0
		h = 0
		subStringLength = sys.maxsize
		count = len(target)
		while r < len(string):
			if target_dic[string[r]] > 0:
				count -= 1
			target_dic[string[r]] -= 1
			r += 1

			while count == 0:
				if r - l  < subStringLength:
					subStringLength = r - l
					h=l
				target_dic[string[l]] += 1
				if target_dic[string[l]] > 0:
					count += 1
				l += 1
		return "" if subStringLength == sys.maxsize else string[h:h+subStringLength]










so = Solution()
print(so.minWindow(S,T))


