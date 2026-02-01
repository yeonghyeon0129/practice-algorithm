while True:
    _input = input()
    if _input == '0':
        break
    else:
        num_list = list(_input)
        result = 'no'
        n_len = len(num_list)
        if n_len == 1:
            print('yes')
            continue
        m, n  = divmod(n_len, 2)

        f_num = int(''.join(num_list[:m]))
        if n == 1:
            m += 1
        b_num = int(''.join(list(reversed(num_list[m:]))))
        if f_num == b_num:
            result = 'yes'

        print(result)
