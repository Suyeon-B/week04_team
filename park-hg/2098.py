import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[1e9]*N for _ in range(1<<N)]

for S in range(1<<N):
    for i in range(N):
        for j in range(N):
            if S & (1<<j):
                dp[S][i] = min(dp[S][i], dp[S])