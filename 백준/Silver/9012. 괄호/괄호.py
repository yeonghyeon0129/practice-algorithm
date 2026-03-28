import sys

count = int(sys.stdin.readline())
result_list = []
T = "YES"
F = "NO"

for i in range(count):
    tmp_count = 0
    test_vps = list(sys.stdin.readline())[:-1]
    for t in test_vps:
        if t == '(':
            tmp_count += 1
        else:
            tmp_count -= 1
        
        if tmp_count < 0:
            break
    if tmp_count == 0:
        result_list.append(T)
    else:
        result_list.append(F)

for result in result_list:
    print(result)
