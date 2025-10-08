num = int(input())
result = list()

for n in range(num):
    result.append(sum(list(map(int, input().split(" ")))))

for data in result:
    print(data)
