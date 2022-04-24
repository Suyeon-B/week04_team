import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

n_list = []

for i in range(n) :
    start, end = map(int, input().split())
    n_list.append([start, end])

# print(n_list)
n_list.sort(key = lambda x : (x[1], x[0]))
min_time = n_list[0][1]     #첫번째 종료점으로 시작점 잡았어요
# n_list.sort(key = lambda x : x[0])

cnt = 1
print(n_list)


for i in range(len(n_list)):
    
    temp = 1000001
    if n_list[i][0] < min_time :
        continue

    for j in range(i, len(n_list)) : # 다음 것 중에 고르려고
        
        if n_list[j][0] > temp :
            break

        if n_list[j][0] >= min_time :         #시작 시간이 전의 끝 시간 보다 크거나 같을 때 돌아가야
            temp = min(temp, n_list[j][1])

    min_time = temp
    # print(min_time)
    cnt += 1
    
print(cnt)