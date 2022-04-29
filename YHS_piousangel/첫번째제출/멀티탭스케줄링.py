import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

dic = {}                            #누가 많이 나오냐가 아니라 누가 더 빨리나오냐? 계속 다음인덱스를 저장해줘야 겠다.

N, K = map(int, input().split())

num_list = list(map(int, input().split()))
blank_list = []
# nextIdx_list = []

for i in range(N):
    blank_list.append(num_list[i])          #인덱스 저장
#     blank_list.append(num_list[i])

# for num in num_list :
#     if num not in dic :
#         dic[num] = 1
#     else:
#         dic[num] += 1

# print(blank_list)
# print(dic)
answer = 0
for i in range(N, K):
    print(blank_list)
    temp_list = [] # 꽂혀있는 전기용품중 마지막에 나오는 것 찾으려고 만듬
    temp_cnt = 0 #들어있는거 대신 다른게 먼저 튀어나올경우
    for j in range(i, K) :          #구멍에 꽂혀있는 것중 누가 더빨리 나오는지 확인해야함

        if num_list[j] in blank_list :
            temp_list.append(num_list[j])
        else:
            temp_cnt += 1

        if len(temp_list) == N:            #겹칠수도 안겹칠 수도 있구나
            if temp_cnt != 0:  #그 전에 앞에 머가 나왔을 때
                del blank_list[-1]
        
        elif len(temp_list) < N :
            remove_cnt = N - len(temp_list) #제거할 갯수
            for r in range(remove_cnt):
                del blank_list[-1-r]

            # for blank in blank_list :
            #     if blank not in temp_list:
            #         blank_list.remove(blank)     #늦게나온 전기용품 제거
            #     else:
            #         break

    if len(blank_list) != N :            #변경사항이 있으면
        add_cnt = N - len(blank_list)
        for a in range(add_cnt):
            blank_list.append(num_list[i+a])            #idx를 다음 포문으로 넘겨줘야해
            answer += add_cnt

print(answer)
