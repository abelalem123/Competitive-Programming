def myFunc():
    x = int(input())
    words = input()
    cnt={}

    word = ''
    for letter in words:
        cnt[letter] =cnt.get(letter,0)+1
    for val in cnt.values():
        if x != val:
            return -1
    for i in range(x):
        for key in cnt.keys():
            word = word + str(key)
    return word


print(myFunc())
