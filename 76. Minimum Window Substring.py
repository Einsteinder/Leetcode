S = "cabwefgewcwaefgcf"
T = "cae"

class Solution:
	def minWindow(self, s, t):
		def ifcontain(sub,t):
			listT = list(t)
			for i in range(len(sub)):
				if sub[i] in listT:
					listT.remove(sub[i])
				print(listT)
			if len(listT)>0:
				return False
			else:
				return True

		if not ifcontain(s,t):
			return ""


		result = s
		lenth =len(s)
		for l in range(0,len(s)):
			occurDic = {}

			for i in range(l,len(s)):
				if s[i] in t:
					if s[i] in occurDic:
						occurDic[s[i]] += 1
					else:
						occurDic[s[i]] = 1
			for i in range(len(s)-1,l-1,-1):
				if s[i] in occurDic:
					if occurDic[s[i]]>t.count(s[i]):
						occurDic[s[i]] -= 1
					else:
						rightIndex = i
						break
			if ifcontain(s[l:rightIndex+1],t):
				if len(s[l:rightIndex+1])<lenth:
					result = s[l:rightIndex+1]
					lenth = len(s[l:rightIndex+1])
			print("l",s[l])
		return result

so = Solution()
print(so.minWindow(S,T))


