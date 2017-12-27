bits=[1,1,0]

class Solution:
	def isOneBitCharacter(self, bits):
		i = 0
		while i < len(bits):
			if bits[i]==0:
				if i == len(bits)-1:
					return True
				i += 1
			if bits[i]==1:
				if i == len(bits)-2:
					return False
				i += 2


x=Solution()
print(x.isOneBitCharacter(bits))