import sys

def calc_value(tmp_value, t_flag):
    result = 0
    if tmp_value == 0:
        pass
    elif t_flag:
        for i in range(1, 10):
            value = (10 * i - tmp_value) / 3
            if value % 1 == 0:
                result = int(value)
                break
    else:
        result = 10 - tmp_value
    
    return result
    
isbn_list = list(sys.stdin.readline()[:-1])
tmp_value = 0
t_flag = False

for i, num in enumerate(isbn_list):
    if num == '*':
        if i%2 == 1:
            t_flag = True
        continue

    if i%2 == 1:
        tmp_value += int(num) * 3
    else:
        tmp_value += int(num)

tmp_value = tmp_value % 10
result = calc_value(tmp_value, t_flag)

print(result)
