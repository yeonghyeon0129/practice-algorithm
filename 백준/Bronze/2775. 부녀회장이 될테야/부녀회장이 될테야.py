def sum_row(count_list, _k, cur=0):
    if _k == cur:
        return sum(count_list)
    _count_list=list()
    for i, count in enumerate(count_list, start=1):
        _count_list.append(sum(count_list[0:i]))
    return sum_row(_count_list, _k, cur+1)

def sum_conf(k, n):
    result = 0
    count_list = [i for i in range(1, n+1)]
    result = sum_row(count_list, k-1)
    return result

T = int(input())
result_list = list()

for i in range(0, T):
    k = int(input())
    n = int(input())
    if n == 1:
        result = n
    else:
        result = sum_conf(k, n)
    result_list.append(result)

for result in result_list:
    print(result)