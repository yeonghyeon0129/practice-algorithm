num_list = list()
for i in range(0, 9):
    num_list.append(int(input()))

max_value = max(num_list)
print(max_value)
print(num_list.index(max_value) + 1)
