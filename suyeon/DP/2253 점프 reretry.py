from sys import stdin
import math
stdin = open("DP/input.txt",'r')
input = stdin.readline

n, m = map(int, input().split())
s_rocks = [int(input()) for _ in range(m)]

dp = [[float('inf')]*(int(math.sqrt(2*n))+2) for _ in range(n+1)]
dp[1][0] = 0 # 1번 돌의 점프 수는 0번으로 초기화

for i in range(2, n+1): # 2번 돌 부터 점프 재개
    if i in s_rocks:
        continue
    for j in range(1, int(math.sqrt(2*i))+1): # 점프 폭은 1 ≤ j ≤ i(i+1)/2 ≒ sqrt(2 * i)
        dp[i][j] = min(dp[i-j][j], dp[i-j][j-1], dp[i-j][j+1])+1

if min(dp[n]) == float('inf'):
    print(-1)
else:
    print(min(dp[n]))