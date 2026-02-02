n = input()
score_list= list(map(int, input().split(' ')))
m = max(score_list)
f_result = 0
for score in score_list:
    f_result += score/m*100
    
print(f_result/int(n))