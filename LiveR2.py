# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
A=[2,1,1,3,2,1,1,3]#3
#A=[7,5,2,7,2,7,4,7]# 6
#A=[7,3,7,3,1,3,4,1]
def solution(A):
    targetNumer = set(A)
    def containTarget(subS,target):
        target = list(target)
        for i in range(len(subS)):
            if subS[i] in target:
                target.remove(subS[i])
        if len(target) > 0:
            return False
        else:
            return True
    positionList = []
    for index in range(len(A)):
        positionList.append(index)
    leftIndex = positionList[0]
    rightIndex = positionList[0]
    print(positionList)
    def nextPosition(elemindex):
        try:
            return positionList[positionList.index(elemindex) + 1]
        except:
            return positionList[-1] + 2
    length=len(A)
    while rightIndex <= positionList[-1]:
        if containTarget(A[leftIndex:rightIndex + 1], targetNumer):
            if len(A[leftIndex:rightIndex + 1]) <= length:
                result = A[leftIndex:rightIndex + 1]
                length = len(A[leftIndex:rightIndex + 1])
            leftIndex = nextPosition(leftIndex)
        else:
            rightIndex = nextPosition(rightIndex)

    return length
print(solution(A))