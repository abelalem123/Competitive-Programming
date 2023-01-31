s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
n=0
for i in range(len(s1)):
    if ord(s1[i]) < ord(s2[i]):
        n=-1
        break
    elif ord(s1[i]) > ord(s2[i]):
        n=1
        break
print(n)
