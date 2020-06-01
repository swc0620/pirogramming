num = int(input())

for i in range(num):
    paren_list = input()
    i = 0
    while i < 26:
        if '()' in paren_list:
            paren_list = paren_list.replace('()', '')
        else:
            break
        i = i + 1

    if len(paren_list) == 0:
        print('YES')
    else:
        print('NO')
        