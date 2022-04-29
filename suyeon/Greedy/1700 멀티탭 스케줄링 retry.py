# 반례 존재
# 새로 꽂는 시점에서 플러그에 이미 꽂혀있는 제품 중 제일 마지막에 등장하는 것을 뽑아야 함.
from sys import stdin
from collections import defaultdict, deque
stdin = open("Greedy/input.txt",'r')
input = stdin.readline

n, k = map(int, input().strip().split())
elect = list(map(int, input().strip().split()))
result = 0

elect_pri = defaultdict(list)
temp = list(reversed(elect))
for i in range(k):
    idx = k-1-i
    elect_pri[temp[i]] += [idx]

in_plug = defaultdict(int)
s_idx = i = 0
while i < n: # 플러그 개수만큼 우선 사용 차감 반영
    if not in_plug[elect[i]]: # 아직 플러그에 안 꽂은 제품이면
        in_plug[elect[i]] = 1 # 플러그에 사용중 표시
    # 이미 꽂혀있는 제품이면
    s_idx += 1
    i += 1

for i in range(s_idx, len(elect)):
    if not in_plug[elect[i]]: # 아직 플러그에 안 꽂은 제품이면 무언가 뽑아야 함
        del in_plug[elect[i]]
        # 플러그에 꽂힌 제품 중에 reverse idx가 작은 것을 뽑는다.
        candidate = deque(in_plug.keys())
        now = candidate.popleft()
        for j in range(len(candidate)):
            if elect_pri[candidate[j]] < elect_pri[now]: # 남겨야 할 제품일 때
                now = candidate[j]
            else: 
                now = candidate[j]
        del in_plug[now]
        result += 1 
        in_plug[elect[i]] = 1 # 플러그에 사용중 표시
        
print(result)