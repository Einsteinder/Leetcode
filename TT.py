#coding=utf-8
import sys



def MinSliceWeight(Matrix):
    lowestWeight = 0
    if len(Matrix) == 0:
        return 0
    for sub in Matrix:
        lowestWeight += sub[0]
    for i in range(len(Matrix[0])):
        currenWeight = Matrix[0][i]
        for j in range(1, len(Matrix)):
            if i == 0:
                currenWeight += min(Matrix[j][i], Matrix[j][i + 1])
            elif i == (len(Matrix[0])-1):
                currenWeight += min(Matrix[j][i - 1], Matrix[j][i])
            else:
                currenWeight += min(Matrix[j][i - 1], Matrix[j][i + 1], Matrix[j][i])
        lowestWeight = min(lowestWeight, currenWeight)
    return lowestWeight



print(MinSliceWeight([[1,2,3,7,-3],[4,5,6,-3,2],[7,-8,9,2,1],[2,3,6,-12,4],[2,3,-6,12,4]]))