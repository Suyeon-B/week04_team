from sys import stdin
from collections import defaultdict
stdin = open("Greedy/input.txt",'r')
input = stdin.readline

n, k = map(int, input().strip().split())
elect = list(map(int, input().strip().split()))
result = 0

in_plug = defaultdict(int)
s_idx = i = 0

while sum(in_plug.values()) < n: # 플러그 개수만큼 우선 사용 차감 반영
    if not in_plug[elect[i]]: # 아직 플러그에 안 꽂은 제품이면
        in_plug[elect[i]] = 1 # 플러그에 사용중 표시
    # 이미 꽂혀있는 제품이면
    s_idx += 1
    i += 1
    if i == k-1:
        break


for i in range(s_idx, len(elect)):
    breaker = False
    if not in_plug[elect[i]]: # 아직 플러그에 안 꽂은 제품이면 무언가 뽑아야 함
        del in_plug[elect[i]]
        # 다음에 안 쓰는 제품이 꽂혀있으면 먼저 뽑는다.
        for e in in_plug.keys():
            if e not in elect[i+1:]:
                del in_plug[e]
                result += 1 
                in_plug[elect[i]] = 1
                now = i
                breaker = True
                break
        
        if  not breaker:
            # 모두 다음에도 사용하는 제품이면,
            # 플러그에 꽂힌 제품들이 언제 사용되는지 보고,
            # 가장 나중에 사용될 제품을 뽑는다.
            candidates = {}
            while True:
                for e in in_plug.keys():
                    for j in range(i, k):
                        if e == elect[j]: # 중복값 들어오면 작은 값으로 넣는 과정 필요
                            candidates[e] = [j, e]
                            break
                break
            
            candidates = sorted(candidates.values(), key= lambda x: x[0], reverse=True)
            del in_plug[candidates[0][1]]
            result += 1
            in_plug[elect[i]] = 1 # 플러그에 사용중 표시
        
print(result)