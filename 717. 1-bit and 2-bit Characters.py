bits=[0,1,0,1,0]

class Solution:
	def isOneBitCharacter(self, bits):
		if bits[-1]==0:
			if bits[-2:len(bits)]==[0,0]:
				return True
			if bits==[1,0]:
				return False
			flag = 1
			for i in range(len(bits)-2,-1,-2):
				print("i",i)
				print("flag",flag)
				print(bits[i-1])
				if i-1>0:
					print(bits[i-1:i+1])
					if bits[i-1:i+1]==[0,1]:
						flag += 1
				if i == 1:
					if bits[i-1:i+1]==[0,1]:
						flag += 1
				if i == 0:
					if bits[i:i+2] == [1,1]:
						flag += 1

				print("flag",flag%2,bool(flag%2))
			return bool(flag%2)
		else:
			return False

x=Solution()
print(x.isOneBitCharacter(bits))