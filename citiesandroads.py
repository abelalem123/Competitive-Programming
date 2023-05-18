n=int(input())
array=[]
for _ in range(n):
    x=input().split()
    array.append(list(map(int,x)))
s=set()
for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j]==1 and (j+1,i+1) not in s:
            s.add((i+1,j+1))
print(len(s))
