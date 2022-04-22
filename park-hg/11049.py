import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

r, c = [], []
for _ in range(N):
    R, C = map(int, sys.stdin.readline().split())
    r += R,
    c += C,

dp = [[1e9]*N for _ in range(N)]

for i in range(N-1):
    dp[i][i+1] = r[i]*r[i+1]*c[i+1]

for k in range(1, N):
    for i in range(N-k):
        dp[i][i+k] = min(dp[i][i+k], )

print(dp)