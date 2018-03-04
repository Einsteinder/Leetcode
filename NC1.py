# Complete the function below.
m=[ ['.','m','.','.'],
    ['.','.','.','.'],
    ['.','.','.','m'],
    ['m','.','.','.'] ]
def  solve_minesweeper(puzzle_array):
	x = [[0 for i in range(len(puzzle_array))] for j in range(len(puzzle_array))]
	adjacentCellofMine = []
	mineList = []
	directlyBelow = []
	directlyRight = []
	shareDic = {}
	shareCorner = []

	for i in range(len(puzzle_array)):
		for j in range(len(puzzle_array)):
			if puzzle_array[i][j]=='m':
				mineList.append((i,j))

	for i,j in mineList:

		if (i-1>=0 and i-1 <len(puzzle_array)) and (j>=0 and j <len(puzzle_array)):
			adjacentCellofMine.append((i-1,j))
		if (i+1>=0 and i+1 <len(puzzle_array)) and (j>=0 and j <len(puzzle_array)):
			adjacentCellofMine.append((i+1,j))		
		if (i>=0 and i <len(puzzle_array)) and (j-1>=0 and j-1 <len(puzzle_array)):
			adjacentCellofMine.append((i,j-1))		
		if (i>=0 and i <len(puzzle_array)) and (j+1>=0 and j+1 <len(puzzle_array)):
			adjacentCellofMine.append((i,j+1))
		if (i-1>=0 and i-1 <len(puzzle_array)) and (j-1>=0 and j-1 <len(puzzle_array)):
			adjacentCellofMine.append((i-1,j-1))			
		if (i+1>=0 and i+1 <len(puzzle_array)) and (j+1>=0 and j+1 <len(puzzle_array)):
			adjacentCellofMine.append((i+1,j+1))
		if (i+1>=0 and i+1 <len(puzzle_array)) and (j-1>=0 and j-1 <len(puzzle_array)):
			adjacentCellofMine.append((i+1,j-1))
		if (i-1>=0 and i-1 <len(puzzle_array)) and (j+1>=0 and j+1 <len(puzzle_array)):
			adjacentCellofMine.append((i-1,j+1))
	for i,j in adjacentCellofMine:
		x[i][j]+=1
	for i,j in mineList:
		if (i+1>=0 and i+1 <len(puzzle_array)) and (j>=0 and j <len(puzzle_array)):
			directlyBelow.append((i+1,j))		
	for i,j in directlyBelow:
		x[i][j]=2
	#rule3
	for i,j in mineList:
		if (i>=0 and i <len(puzzle_array)) and (j+1>=0 and j+1<len(puzzle_array)):
			directlyRight.append((i,j+1))	
	for i,j in directlyRight:
		x[i][j]=0
	#rule4
	for i,j in mineList:
		if i%2==1:
			x[i]=[3*item for item in x[i]]
	#rule5


	for i,j in mineList:
		if (i-1>=0 and i-1 <len(puzzle_array)) and (j-1>=0 and j-1 <len(puzzle_array)):
			shareCorner.append((i-1,j-1))			
		if (i+1>=0 and i+1 <len(puzzle_array)) and (j+1>=0 and j+1 <len(puzzle_array)):
			shareCorner.append((i+1,j+1))
		if (i+1>=0 and i+1 <len(puzzle_array)) and (j-1>=0 and j-1 <len(puzzle_array)):
			shareCorner.append((i+1,j-1))
		if (i-1>=0 and i-1 <len(puzzle_array)) and (j+1>=0 and j+1 <len(puzzle_array)):
			shareCorner.append((i-1,j+1))	

	shareCorner=set(shareCorner)
	for i,j in shareCorner:
		x[i][j]=2*x[i][j]
	#rule6
	for i,j in mineList:
		x[i][j]=-1

	return x

print(solve_minesweeper(m))