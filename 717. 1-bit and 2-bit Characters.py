bits = [1,0, 0]
class Solution:
	def isOneBitCharacter(self, bits):
#		print(len(bits)%2)
		if len(bits)%2==1:
			for i in range(len(bits)-2,-1,-2):
				if bits[i-1:i+1]==[0,1]:
					return False
			return True
		else:
			for j in range(0,len(bits),2):
				if bits[j:j+2]==[0,1]:
					return True
			return False
x=Solution()
print(x.isOneBitCharacter(bits))