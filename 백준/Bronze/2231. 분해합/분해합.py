num = int(input())

half_num = num // 2 
result = 0

for n in range(half_num, num):
    x = 0
    for str_n in list(str(n)):
        x += int(str_n)
    
    if n + x == num:
        result = n
        break

print(result)
