s = input()

length = len(s)
half_length = len(s) // 2

for i in range(1, half_length + 1):
    repeat = length // i
    count = 0
    for j in range(repeat):
        if s[i*j:i*(j+1) - 1] == s[i*(j+1):i*(j+2)-1]:
            count += 1
    print (i, repeat, s, count)