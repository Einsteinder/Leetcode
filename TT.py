def ladderLength( start, end, dic):
    if start == end: return 1
    n = len(start)
    atoz = list(map(chr, range(ord('a'), ord('z') + 1)))
    q, vis, dis = [start], set(), 1
    vis.add(start)
    while q:
        cur = q.pop(0)
        for j in range(n):
            for k in atoz:
                t = cur[:j] + k + cur[j + 1:]
                if t == end:
                    return dis
                if t in dic and t not in vis:
                    q.append(t)
                    vis.add(t)
        dis += 1
    return 0
print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))