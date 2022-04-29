# 버그 해결해야함
from sys import stdin
from collections import Counter, defaultdict, deque
stdin = open("Greedy/input.txt",'r')
input = stdin.readline

n, k = map(int, input().strip().split())
elect = deque(map(int, input().strip().split()))
result = 0

# 사용 빈도 체크
cnt = Counter(elect)
in_plug = defaultdict(int)
s_idx = i = 0
while i < n: # 플러그 개수만큼 우선 사용 차감 반영
    if not in_plug[elect[i]]: # 아직 플러그에 안 꽂은 제품이면
        in_plug[elect[i]] = 1 # 플러그에 사용중 표시
    # 이미 꽂혀있는 애면 cnt 개수만 줄여준다.
    cnt[elect[i]] -= 1 
    s_idx += 1
    i += 1


for i in range(s_idx, len(elect)):
    if not in_plug[elect[i]]: # 아직 플러그에 안 꽂은 제품이면 무언가 뽑아야 함
        # cnt가 남은 제품들 중에, plug에 꽂혀있는 제품이 있나 확인
        # 남은 빈도수와 함께 제품을 담는다.
        temp = []
        for e in cnt.keys():
            if e in in_plug.keys():
                temp.append((e, cnt[e]))
        
        # 남은 빈도수가 낮은 제품을 먼저 뽑는다.
        sorted_temp = list(sorted(temp, key=lambda x: x[1]))
        del in_plug[sorted_temp.pop(0)[0]]
        result += 1

        in_plug[elect[i]] = 1 # 플러그에 사용중 표시
        
    # 이미 꽂혀있는 애면 cnt 개수만 줄여준다.
    cnt[elect[i]] -= 1 

print(result)