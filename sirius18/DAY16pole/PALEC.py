import sys
sys.setrecursionlimit(int(1e9))

nv, ne = map(int, input().split())
adj = [[] for i in range(nv + 1)]
for i in range(ne):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    adj[v1].append(v2)
    adj[v2].append(v1)
sizes = [[] for i in range(nv + 1)]
curt = 0
mint = [-1 for i in range(nv + 1)]
time = [-1 for i in range(nv + 1)]
def findd(v, parent):
    global curt, time, mint, adj, sizes
    assert(time[v] == -1)
    time[v] = curt
    mint[v] = curt
    curt += 1
    ch = 0
    for nex in adj[v]:
        if nex == parent:
            continue
        if time[nex] == -1:
            bef = curt
            findd(nex, v)
            aft = curt
            ch += 1
            if (parent != -1 and mint[nex] >= time[v]) or (parent == -1 and ch > 1):
                sizes[v].append(aft - bef)
            mint[v] = min(mint[v], mint[nex])
        else:
            mint[v] = min(mint[v], time[nex])
findd(0, -1)
for i in range(nv):
    res = 0
    if len(sizes[i]) != 0:
        summ = 0
        for x in sizes[i]:
            summ += x
        assert(summ < nv - 1)
        sizes[i].append(nv - 1 - summ)
        for x in sizes[i]:
            res += x * (nv - 1 - x)
    assert(res % 2 == 0)
    res //= 2
    res += nv - 1
    print(res)#end.