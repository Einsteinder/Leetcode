#coding=utf-8
import sys

n = sys.stdin.readline().strip()
n=int(n)
resultL = [2]
for index in range(2,n+1):
    for item in resultL:
        if index%item==0:
            resultL.append(index/item)
        resultL.append(index)
result = 1
for i in resultL:
    result*=i
print(result%987654321)


