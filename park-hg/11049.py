import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

r, c = [], []
for _ in range(N):
    R, C = map(int, sys.stdin.readline().split())
    r += R,
    c += C,

dp = [[1<<31]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for j in range(N):
    for i in range(N-j):
        for k in range(j):
            dp[i][i+j] = min(dp[i][i+j], dp[i][i+k]+dp[i+k+1][i+j]+r[i]*r[i+k+1]*c[i+j])

print(dp[0][-1])