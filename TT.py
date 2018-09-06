import collections
p1 = [3] * 3
p2 = [3,2,2]

pc = collections.Counter(p2)
pc[5] += 3
print(pc)
