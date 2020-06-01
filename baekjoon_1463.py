
# num = int(input())


# def count(number):
#     route = 999999999999999
#     if number == 0 or number == 1:
#         return 0
#     elif number % 2 == 0:
#         route = min(route, count(number/2)) + 1
#     elif number % 3 == 0:
#         route = min(route, count(number/3)) + 1
#     else:
#         route = min(route, count(number-1) + 1)
    
#     return route
    

# print(count(num))
    

number = int(input())
result = [0, 0, 1, 1]

for num in range(4, number + 1):
    if num % 3 == 0 and num % 2 != 0:
        count = min(result[num//3] + 1, result[num - 1] + 1)
    elif num % 2 == 0 and num % 3 != 0:
        count = min(result[num//2] + 1, result[num - 1] + 1)
    elif num % 3 == 0 and num % 2 == 0:
        count = min(result[num//3] + 1, result[num//2] + 1, result[num - 1] + 1)
    else:
        count = result[num - 1] + 1
    result.append(count)
print(result[number])
