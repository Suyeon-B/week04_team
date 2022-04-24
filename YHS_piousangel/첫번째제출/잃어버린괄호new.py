import sys

sys.stdin = open('sample.txt')
susik_str = input().rstrip()

num_list = []
cal_list = []
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

visited = [False] * len(num_list) # + 인 것들만 방문체크 해주려고
total = 0
# idx = 0

for i in range(len(cal_list)):
    if cal_list[i] == '-' :                      #마이너스 이후인 것들은 싹다 마이너스 처리가능하지 않나
        for j in range(i+1, len(num_list)):
            total -= int(num_list[j])
            visited[j] = True
        break
# print(num_list,"num_list")
# print(cal_list,"cal_list")
# print(visited,"visited")
# print(total,"total")
for i in range(len(visited)):
    if visited[i] == False:
        total += int(num_list[i])

print(total)
