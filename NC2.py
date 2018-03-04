# Complete the function below.
s=['GoCardinals', 'Doge', 'nExTcapITalxnextcapital', 'ThreeSThree']

def  strengthen_passwords(passwords):
	listOfString =[]
	for item in passwords:
		listOfString.append(list(item))
	for item in listOfString:
		for i,j in enumerate(item):
			if j=="s" or j=="S":
				item[i]=5
	for item in listOfString:
		if len(item)%2==1 and str(item[len(item)//2]) in "0123456789":
			item[len(item)//2]=str(2*int(item[len(item)//2]))
	afterPasswords=[]
	afterPasswordsList=[]
	for item in listOfString:
		afterPasswords.append("".join(map(str,item)))
	for item in afterPasswords:
		afterPasswordsList.append(list(item))
	print(afterPasswordsList)
	for item in afterPasswordsList:
		if len(item)%2==0:
			temp = item[0]
			if temp.islower():
				temp=temp.upper()
			else:
				temp = temp.lower()
			item[0]=item[-1]
			item[-1]=temp
			if item[0].islower():
				item[0]=item[0].upper()
			else:
				item[0] = item[0].lower()
	beforeResult =[]
	for item in afterPasswordsList:
		beforeResult.append("".join(map(str,item)))
	print(beforeResult)
	for index in range(len(beforeResult)):
		if "nextcapital" in beforeResult[index].lower():
			print("asdafsdfa----")
			nextIndex = beforeResult[index].lower().index("next")
			listItem = list(beforeResult[index])
			reversedNext = reversed(listItem[nextIndex:nextIndex+4])
			reversedNextList = list(reversedNext)
			for j in range(len(reversedNextList)):
				listItem[nextIndex+j]=reversedNextList[j]
			listItem="".join(map(str,listItem))
			beforeResult[index] = listItem

	print(beforeResult)
strengthen_passwords(s)