import sys
sys.stdin = open('input.txt')


N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if W[i][j] == 0:
            W[i][j] = 1e9

dp = [[1e9]*N for _ in range(1<<N)]
dp[0][0] = 0
for S in range(1<<N):
    for i in range(N):
        for j in range(N):
            if S & (1<<j):
                dp[S][i] = min(dp[S][i], dp[S&(~(1<<j))][j] + W[j][i])

print(dp[-1][0])