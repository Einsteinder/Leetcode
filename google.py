"""
Inputs:
    (string) s = "abccbaabccba"
Output:
    (int) 2

Inputs:
    (string) s = "abcabcabcabc"
Output:
    (int) 4
"""
s = "eeeeeeaaaaff"
def brute(inputString):
	resultDic = {}
	for i in range(1,int(len(inputString))):
		resultDic[i]=[]
		for j in range(0,len(inputString),i):

			resultDic[i].append(inputString[j:j+i])
	newDic = {}
	for item in resultDic.items():
		newDic[item[0]]=set(item[1])
	result = min(newDic.items(),key=lambda x:len(x[1]))
	print(result)
	if len(result[1])==1:
		return int(len(inputString)/result[0])
	else:
		return 1

print(brute(s))

