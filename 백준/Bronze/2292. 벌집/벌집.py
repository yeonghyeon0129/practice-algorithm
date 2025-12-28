destination = int(input())

result = 1
inc_num = 0
while True:
    _inc_num = inc_num + result - 1
    if destination <= (6 * _inc_num + 1):
        break
    result += 1 
    inc_num = _inc_num
    

print(result)