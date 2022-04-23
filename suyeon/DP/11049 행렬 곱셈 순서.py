import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline


n = int(input().strip())
matrix = []
for i in range(n):
    matrix.append(tuple(map(int, input().strip().split())))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(i+1, n+1):
        for k in range(i, j+1):
            if i == j:
                dp[i][j] = 0
            elif j-i == 1:
                dp[i][j] = matrix[i][0] * matrix[i][1] * matrix[j][1]
            else:
                dp[i][j] = min(dp[i][j], matrix[i][0] * matrix[i][1] * matrix[j][1] + dp[i][k] + dp[k+1][j])

print(dp[n][n])
