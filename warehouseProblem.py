from collections import defaultdict

ids = list(map(int, input().split()))
vals = list(map(int, input().split()))

def solve(ids, vals):
    info = defaultdict(int)
    
    for i in range(len(ids)):
        if vals[i] > info[ids[i]]:
            info[ids[i]] = vals[i]

    return sum(info.values())

print(solve(ids,vals))