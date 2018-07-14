#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    final = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(float, line.split()))
        result={}
        for ndex,n in enumerate(values[1:]):
            for mdex,m in enumerate(values[1:ndex]):
                result[(m,n)]=m/n
        sortedResult = sorted(result.items(),key=lambda x:x[1])

        final.append((int(sortedResult[int(values[0])-1][0][0]),int(sortedResult[int(values[0])-1][0][1])))


for item in final:
    print(item)