def fetch():
    return map(int, input().split(" "))
n, x = fetch()
data_list = [result for result in list(fetch()) if x > result]
for data in data_list:
    print(data, end=" ")