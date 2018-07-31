def pali(s):
	table = []
	for i in range(len(s)):
		tableRow = []
		for j in range(len(s)):
			if i == j:
				tableRow.append(1) 
			else:
				tableRow.append(0)
		table.append(tableRow)
	print(table)
	#k = 2
	for i in range(len(s)-1):
		if s[i]==s[i+1]:
			table[i][i+1] = 1
	print(table)
	k = 3
	while k <= len(s):
		i = 0
		while i < len(s) - k:
			if table[i+1][i+k-2] and s[i]==s[i+k-1]:
				table[i][i+k-1] = 1
			i += 1
		k += 1
	maxLength = 0
	result = ""
	for i in range(len(table)):
		for j in range(len(table)):
			if table[i][j] == 1 and j-i+1>maxLength:
				maxLength = j-i+1
				result = s[i:j+1]
	return result

print(pali("cbbd"))



			 
