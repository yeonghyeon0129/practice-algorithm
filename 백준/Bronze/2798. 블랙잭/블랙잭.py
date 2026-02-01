def get_result(m, num_list):
    result = 0
    for num in num_list:
        for s_num in num_list:
            if num == s_num:
                continue
            for t_num in num_list:
                if num == t_num:
                    continue
                elif s_num == t_num:
                    continue
                m_result = num + s_num + t_num
                if m_result == m:
                    result = m
                    return result
                elif m_result < m and m_result > result:
                    result = m_result
    return result

input_list= list(map(int, input().split()))
num_count = input_list[0]
m = input_list[1]

num_list = list(map(int, input().split()))

num_list = sorted(num_list)

result = get_result(m, num_list)
print(result)