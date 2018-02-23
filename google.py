"""
For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.
[210111, 122221, 102212]
"""
number = 210111
count = 0 
def answer(n, b):
	resultList = []
	def inanswer(n,b):
		originalN =n
		numberList = []
		for i in str(n):
			numberList.append(i)
		x = sorted(numberList,reverse=True)
		y = sorted(numberList)
		zList =[]
		lendOne = 0
		for index in range(len(x)-1,-1,-1):
			x[index]=int(x[index])-lendOne
			if int(x[index]) >= int(y[index]):
				resultNumber = int(x[index])-int(y[index])
				lendOne = 0
			else:
				resultNumber = b-(int(y[index])-int(x[index]))
				lendOne = 1
			zList.insert(0,resultNumber)
			zList =[str(i) for i in zList]
		n="".join(zList)
		print(n)
		b=b
		if n in resultList:
			print(resultList.index(n))
			print(len(resultList[resultList.index(n):]))
		else:
			resultList.append(n)
			inanswer(n,b)


		
	inanswer(n,b)
	print(resultList)



print(answer(210022,3))

