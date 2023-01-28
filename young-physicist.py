n = int(input())
s1 = 0
s2 = 0
s3 = 0
for i in range(n):
    x = input().split()
    s1 += int(x[0])
    s2 += int(x[1])
    s3 += int(x[2])

if s1==0 and s2==0 and s3==0:
    print('YES')
else:
    print('NO')
