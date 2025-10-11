try_cnt = int(input())
result_list = list()
for i in range(0, try_cnt):
    num, string = input().split(" ")
    result_list.append(''.join([s * int(num) for s in list(string)]))

for result in result_list:
    print(result)