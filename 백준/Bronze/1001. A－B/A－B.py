input_data = list(map(int, input().split()))

result = 0
for i, data in enumerate(input_data):
    if i == 0:
        result = data
    else:
        result -= data

print(result)