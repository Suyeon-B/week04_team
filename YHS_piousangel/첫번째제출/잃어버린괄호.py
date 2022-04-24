import sys

sys.stdin = open('sample.txt')
susik_str = input().rstrip()

num_list = ['0']
cal_list = ['+']
idx = 0

for i in range(len(susik_str)) :
    if susik_str[i] == '+' or susik_str[i] == '-':
        num_list.append(susik_str[idx:i])
        if susik_str[i] == '+' :
            cal_list.append('+')
        else:
            cal_list.append('-')         #cal_list 에서 - 뒤에 플러스 된게 가장 큰걸고르나?
        idx = i+1

num_list.append(susik_str[idx:])

# print(num_list)
# print(cal_list)
total = 0                         # 총합 구하려고
total_list = []
visited = [False] * len(num_list) # + 인 것들만 방문체크 해주려고
for i in range(len(cal_list)):
    if cal_list[i] == '+' :
        if visited[i] == False :         #첫 더하기
            total += int(num_list[i]) + int(num_list[i+1])     
            visited[i] = True
            visited[i+1] = True
        else:
            total += int(num_list[i+1])  #연속된 더하기
            visited[i+1] = True
    else:
        total_list.append(total)
        total = -int(num_list[i+1])

total_list.append(total)

# if visited[-1] != True:
#     total_list.append(int(num_list[-1]))  #빼기 한번이라 마지막 숫자가 계산 안될수 있어서
print(sum(total_list))

# print(total_list)
# answer = 0
# if len(total_list) == 1 :
#     print(sum(total_list))
# else:
#     for i in range(len(total_list)):
#         if i == 0 :
#             answer = total_list[i]
#         else:
#             answer -= total_list[i]
#     print(answer)

# for i in range(len(visited)):        
#     if visited[i] == False:                    #마이너스만 남은 상황
#         if i == 0:
#             total = -total + int(num_list[i])
#         else:
#             total -= int(num_list[i])
       

# print(total)
