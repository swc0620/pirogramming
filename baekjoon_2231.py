index = 0

num = int(input())
if 10 <= num <= 99:
    for j in range(num - 16, num) and j - 16 > 0:
        digit_sum = sum(map(int, str(j)))
        if digit_sum + j == num:
            print(j)
            index = j
            break
elif 100 <= num <= 999:
    for j in range(num - 24, num):
        digit_sum = sum(map(int, str(j)))
        if digit_sum + j == num:
            print(j)
            index = j
            break
elif 1000 <= num <= 9999:
    for j in range(num - 33, num):
        digit_sum = sum(map(int, str(j)))
        if digit_sum + j == num:
            print(j)
            index = j
            break
elif 10000 <= num <= 99999:
    for j in range(num - 42, num):
        digit_sum = sum(map(int, str(j)))
        if digit_sum + j == num:
            print(j)
            index = j
            break
elif 100000 <= num <= 999999:
    for j in range(num - 46, num):
        digit_sum = sum(map(int, str(j)))
        if digit_sum + j == num:
            print(j)
            index = j
            break
if index == 0:
    print('%d' %0)




# list = []
# answer = []

# def digit_num(num):
#     global unit
#     list.append(unit)
#     while num != 0:        
#         list.append(num // 10)
#         num = num // 10
#     print(list)

# num_str = input()
# digit = len(num_str)
# number = int(num_str)
# start = number - (10 * digit)
# for i in range(start, number):
#     digit_i = len(str(i))
#     if digit_i == digit:
#         string_i = str(i)
#         unit = int(string_i[digit - 1])
#     else:
#         string_i = str(i)
#         unit = int(string_i[digit_i - 1])
#     digit_num(i)
#     digit_num_sum = sum(list)
#     if i == digit_num_sum + i:
#         answer.append(i)
#     print(digit_num_sum)
#     list.clear()
# print(answer)