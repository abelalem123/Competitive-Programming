def swap_case(s):
    val=""
    for x in s:
        if x.isupper():
            val=val+x.lower()
        elif x.islower():
            val=val+x.upper()
        else:
            val=val+x
    return val
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
