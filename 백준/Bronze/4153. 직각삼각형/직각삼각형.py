while True:
    result = "wrong"
    side_list = list(map(int, input().split(" ")))
    if all(x == 0 for x in side_list):
        break
    m = max(side_list)
    side_list.remove(m)
    if side_list[0]**2 + side_list[1]**2 == m**2:
        result = "right"
    print(result)
