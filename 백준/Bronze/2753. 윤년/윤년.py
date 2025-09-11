num = int(input())

result = 0
if num % 4 == 0 and num % 100 != 0:
    result = 1
elif num % 400 == 0:
    result = 1

print(result)