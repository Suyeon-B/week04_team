import sys
import math
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
smalls = set(int(sys.stdin.readline()) for _ in range(M))

max_v = int((-1+math.sqrt(1+9*(N-1)))/2)
dp = [[1e9]*(max_v+1) for _ in range(N+1)]
dp[1][0] = 0
for i in range(1, N+1):
    for v in range(1, max_v+1):
        if i+v <= N:
            if i+v in smalls:
                continue
            if v+1 > max_v:
                dp[i+v][v] = min(dp[i+v][v], min(dp[i][v-1], dp[i][v])+1)
            else:
                
                dp[i+v][v] = min(dp[i+v][v], min(dp[i][v-1], dp[i][v], dp[i][v+1])+1)

ans = min(dp[-1])
print(-1 if ans==1e9 else ans)
