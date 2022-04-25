import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

dic = {}                            #누가 많이 나오냐가 아니라 누가 더 빨리나오냐? 계속 다음인덱스를 저장해줘야 겠다.

N, K = map(int, input().split())    #구멍수, 멀티탭 확인 수

num_list = list(map(int, input().split()))

# print(num_list)
blank_list = []
# # nextIdx_list = []

for i in range(N):
    blank_list.append(num_list[i])          #구멍에 들어있는 


# if N == 1 :
#     print(K)
# else:
#     answer = 0

answer = 0

for i in range(N, K): #앞에서 부터 가면서
    temp_list = []
    temp_cnt = 0
    print(blank_list)
    if num_list[i] in blank_list:
        continue

    if len(blank_list) < N :              #제거해서 구멍이 쉬고있으면
        blank_list.append(num_list[i])
        continue

    for j in range(K-1, i, -1):  #뒤에서부터 확인해줘
        
        if num_list[j] in blank_list :
            # blank_list.remove(num_list[j])  #뒤에 어팬드 된게 앞에 있는거
            # blank_list.append(num_list[i])
            temp_list.append(j)   #앞에 있는게 빠질것

    if len(temp_list) == N :
        blank_list.remove(blank_list[temp_list[0]])
    else :
        for blank in blank_list :
            if blank != blank_list[temp_list[0]]:
                blank_list.remove(blank)

print(answer)     


import sys
input = sys.stdin.readline

N, K = map(int, input().split())

multitap = list(map(int, input().split()))

plugs = []
count = 0

for i in range(K):
  # 있으면 건너 뛴다.
  if multitap[i] in plugs:
    continue
  
  # 플러그가 1개라도 비어 있으면 집어넣는다.
  if len(plugs) < N:
    plugs.append(multitap[i])
    continue
  
  multitap_idxs = [] # 다음 멀티탭의 값을 저장.
  hasplug = True

  for j in range(N):
  	# 멀티탭 안에 플러그 값이 있다면
    if plugs[j] in multitap[i:]:
      # 멀티탭 인덱스 위치 값 가져오기.
      multitap_idx = multitap[i:].index(plugs[j])
    else:
      multitap_idx = 101
      hasplug = False

    # 인덱스에 값을 넣어준다.
    multitap_idxs.append(multitap_idx)
    
    # 없다면 종료
    if not hasplug:
      break
  
  # 플러그를 뽑는다.
  plug_out = multitap_idxs.index(max(multitap_idxs))
  del plugs[plug_out] # 플러그에서 제거
  plugs.append(multitap[i]) # 플러그에 멀티탭 값 삽입
  count += 1 # 뽑았으므로 1 증가

print(count)
            
        # if len(temp_list) == N :      #다 중복

        #     if num_list[i] == temp_list[0] :
        #         blank_list.remove(temp_list[1]) # 다음 것 제거
        #         answer += 1
        #     else:
        #         blank_list.remove(temp_list[0])
        #         answer += 1
        # else:
        #     temp_cnt = N - len(temp_list) #리스트에서 빼줄 개수
        #     print(temp_cnt)
        #     for j in range(temp_cnt):
        #         blank_list.remove(temp_list[j])       #안겹친 수만큼 제거해줘야죠
        #         answer += 1



