def countSwaps(a):
    # Write your code here
    count=0
    for j in range(len(a)):
        for i in range(1,len(a)-j):
            if a[i-1]>a[i]:
                count+=1
                a[i-1],a[i]=a[i],a[i-1]
    x="Array is sorted in {} swaps.".format(count)
    print(x)
    x="First Element: {}".format(a[0])
    print(x)
    x="Last Element: {}".format(a[-1])
    print(x)
