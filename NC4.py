# Complete the function below.
s=9
m=[[1, 10], [1, 6], [2, 8], [3, 5]]
def  max_florists(path_length, florist_intervals):
	pathBacket = []
	for item in florist_intervals[0:3]:
		pathBacket.append(item)
	maxLowerNumber = max(pathBacket,key=lambda x:x[0])[0]
	minUpperNumber = min(pathBacket,key=lambda x:x[1])[1]
	print(maxLowerNumber)
	print(minUpperNumber)
	for item in florist_intervals[3:]:
		if item[-1]<maxLowerNumber and minUpperNumber<path_length and maxLowerNumber>=0:
			pathBacket.append(item)
			maxLowerNumber = max(pathBacket,key=lambda x:x[0])[0]
		if item[0]>=minUpperNumber and item[0]<path_length and minUpperNumber<path_length and maxLowerNumber>=0:
			pathBacket.append(item)
			minUpperNumber = min(pathBacket,key=lambda x:x[1])[1]
		if item[-1]>=minUpperNumber and item[0]<path_length and minUpperNumber<path_length and maxLowerNumber>=0: 
			pathBacket.append(item)
			minUpperNumber = min(pathBacket,key=lambda x:x[1])[1]
		if item[0]<minUpperNumber and item[0]<path_length and minUpperNumber<path_length and maxLowerNumber>=0:
			pathBacket.append(item)
			minUpperNumber = min(pathBacket,key=lambda x:x[1])[1]
	return len(pathBacket)

print(max_florists(s,m))

