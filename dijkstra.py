from heapq import *
from collections import defaultdict
from copy import *


#maze =  [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]

def answer(maze):
	mazes = defaultdict(list)
	cantPass = []
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j]==1:
				cantPass.append((i,j))

	for i,j in cantPass:
		wallDownMaze = deepcopy(maze)
		wallDownMaze[i][j] = 0
		mazes[(i,j)] = wallDownMaze
	mazes[(0,0)]=maze
	def dijkstra(maze):
		connections=[]
		for i in range(len(maze)):
			for j in range(len(maze[i])):
				if i + 1 < len(maze) and maze[i+1][j]==0:
					connections.append(((i,j),(i+1,j),1))
				if i - 1 >= 0 and maze[i-1][j]==0:
					connections.append(((i,j),(i-1,j),1))
				if j + 1 < len(maze[i]) and maze[i][j+1]==0:
					connections.append(((i,j),(i,j+1),1))
				if j - 1 >= 0 and maze[i][j-1]==0:
					connections.append(((i,j),(i,j-1),1))
		connectionsDic = defaultdict(list)
		for left, right, cost in connections:
			connectionsDic[left].append((cost,right))
		priorityQ = []
		heappush(priorityQ,(0,(0,0),()))
		visited = set()
		while priorityQ:
			(cost, leftNode,path)= heappop(priorityQ)
			if leftNode not in visited:
				visited.add(leftNode)
				path=(leftNode,path)
				if leftNode == (len(maze)-1,len(maze[-1])-1):
					return cost
				for costRight,Right in connectionsDic.get(leftNode,()):

					if Right not in visited:

						heappush(priorityQ,(costRight+cost,Right,path))

		return float("inf")
	resultList = []
	for key,value in mazes.items():
		resultList.append(dijkstra(value))
	return min(resultList)+1

