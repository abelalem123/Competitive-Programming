first_input = int(input())
x = 0
for i in range(first_input):
    exp = input()
    if '+' in exp:
        x = x + 1
    else:
        x = x - 1
print(x)
