#A = [10,0,8,2,-1,12,11,3]
A = [5,5]


def solution(A):
    # write your code in Python 3.6
    distance ={}
    sortedA = sorted(A)
    for index in range(len(sortedA)-1):
        distance[sortedA[index]]= sortedA[index+1]-sortedA[index]
    maxDistance = max(distance.items(),key=lambda x:x[1])

    print(maxDistance[1]//2)
solution(A)