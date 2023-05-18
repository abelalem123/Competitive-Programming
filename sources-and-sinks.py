n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

ans=[]
src=set()
sink=set()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]==1:
            src.add(i+1)
            sink.add(j+1)
newsrc=[]
newsink=[]
for i in range(1,n+1):
    if i not in src:
        newsink.append(i)


for i in range(1,n+1):
    if i not in sink:
        newsrc.append(i)
        
print(len(newsrc),*newsrc)
print(len(newsink),*newsink)
