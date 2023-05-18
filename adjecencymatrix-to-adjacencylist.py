n=int(input())

array=[]
for _ in range(n):
    array.append(list(map(int,input().split())))
from collections import  defaultdict

graphs=defaultdict(list)
for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j]==1:
            graphs[i+1].append(j+1)
for k,v in graphs.items():
    print(len(v),*v)
