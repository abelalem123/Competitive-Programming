user_name = input()
dist_name = set()
for x in user_name:
    dist_name.add(x)
if len(dist_name) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
