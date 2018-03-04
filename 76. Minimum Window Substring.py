#S = "cabwefgewcwaefgcf"
#T = "cae"
S = "a"
T = "a"
#S="ask_not_what_your_country_can_do_for_you_ask_what_you_can_do_for_your_country"
#T="ask_country"
#S = "ADOBECODEBANC"
#T = "ABC"
class Solution:
	def minWindow(self, s, t):
		def ifcontain(sub,t):
			listT = list(t)
			for i in range(len(sub)):
				if sub[i] in listT:
					listT.remove(sub[i])
			if len(listT)>0:
				return False
			else:
				return True

		if not ifcontain(s,t):
			return ""


		result = ""
		length =len(s)
		elementIndexList = []

		for i in range(len(s)):
			if s[i] in t:
				elementIndexList.append(i)
		def nextElement(elemindex):
			try:
				return elementIndexList[elementIndexList.index(elemindex)+1]
			except:
				return elementIndexList[-1]+2
		l = elementIndexList[0]
		r = elementIndexList[0]
		while r <=elementIndexList[-1]:
			if ifcontain(s[l:r+1],t):
				if len(s[l:r+1])<=length:
					result=s[l:r+1]
					length=len(s[l:r+1])
				l = nextElement(l)
			else:
				r = nextElement(r)

		return result

so = Solution()
print(so.minWindow(S,T))


