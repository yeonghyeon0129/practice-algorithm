n = input()
result = 0
for i, v in enumerate(list(input())):
    num = ord(v) - ord('a') + 1
    result += num * 31 ** (i)

print(result % 1234567891)