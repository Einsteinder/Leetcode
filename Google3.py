"""
Test cases
==========

Inputs:
    (int list) l = [4, 3, 10, 2, 8]
    (int) t = 12
Output:
    (int list) [2, 3]

Inputs:
    (int list) l = [1, 2, 3, 4]
    (int) t = 15
Output:
    (int list) [-1, -1]
"""
l = [4, 3, 10, 2, 8]
t = 12
#l=[1, 2, 3, 4]
#t=15
def answer(l,t):
	for index in range(len(l)):
		sumup = 0
		for subIndex in range(index,len(l)):
			sumup+=l[subIndex]
			if sumup == t:
				return [index,subIndex]
	return [-1,-1]
print(answer(l,t))