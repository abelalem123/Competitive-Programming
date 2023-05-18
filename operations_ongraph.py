from collections import  defaultdict
n=int(input())
m=int(input())
graphs=defaultdict(list)
for _ in range(m):
    all=list(map(int,input().split()))
    if all[0]==1:
        graphs[all[1]].append(all[2])
        graphs[all[2]].append(all[1])
    elif all[0]==2:
        print(*graphs[all[1]])
