num_list = list(map(int, input().split(' ')))
result = sum([num ** 2 for num in num_list]) % 10
print(result)